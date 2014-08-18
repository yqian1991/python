import numpy as np
#from matplotlib import pyplot as plt
from scipy.optimize import fmin_l_bfgs_b as bfgs,check_grad,fmin_bfgs,fmin_tnc
from scipy.io import loadmat
import cPickle
 
 
class params:
    
    '''
    A wrapper around weights and biases
    for an autoencoder
    '''
    def __init__(self,indim,hdim,w1 = None,b1 = None,w2 = None,b2 = None):
        self._indim = indim
        self._hdim = hdim
        
        # initialize the weights randomly and the biases to 0
        r = np.sqrt(6.) / np.sqrt((indim * 2) + 1.)
        self.w1 = w1 if w1 is not None else np.random.random_sample((indim,hdim)) * 2 * r - r
        self.b1 = b1 if b1 is not None else np.zeros(hdim)
        
        self.w2 = w2 if w2 is not None else np.random.random_sample((hdim,indim)) * 2 * r - r
        self.b2 = b2 if b2 is not None else np.zeros(indim)
 
 
    def unroll(self):
        '''
        "Unroll" all parameters into a single parameter vector
        '''
        w1 = self.w1.reshape(self._indim * self._hdim)
        w2 = self.w2.reshape(self._hdim * self._indim)
        return np.concatenate([w1,
                               w2,
                               self.b1,
                               self.b2])
 
 
    @staticmethod
    def roll(theta,indim,hdim):
        '''
        "Roll" all parameter vectors into a params instance
        '''
        wl = indim * hdim
        w1 = theta[:wl]
        w1 = w1.reshape((indim,hdim))
        bb =  wl + wl
        w2 = theta[wl: bb]
        w2 = w2.reshape((hdim,indim))
        b1 = theta[bb : bb + hdim] 
        b2 = theta[bb + hdim : bb + hdim + indim]
        return params(indim,hdim,w1,b1,w2,b2)
 
    def __eq__(self,o):
        return (self.w1 == o.w1).all() and \
            (self.w2 == o.w2).all() and \
            (self.b1 == o.b1).all() and \
            (self.b2 == o.b2).all()
 
    @staticmethod
    def _test():
        p = params(100,23)
        a = p.unroll()
        b = params.roll(a,100,23)
        print p == b
        print all(a == b.unroll())
 
        
 
 
class autoencoder(object):
    
    '''
    A horribly inefficient implementation
    of an autoencoder, which is meant to 
    teach me, and not much else.   
    '''
 
    def __init__(self, params, include_weight_decay = True, include_sparsity = True):
        
        self._include_weight_decay = include_weight_decay
        self._include_sparsity = include_sparsity
 
        # this is multiplied against the sparsity delta
        self._beta = 3
        self._sparsity = 0.01
        
        # this is the learning rate
        self._alpha = .01
 
        # this is the weight decay term
        self._lambda = 0.0001
 
        self._netp = params
 
 
    ## ACTIVATION OF THE NETWORK #########################################
 
    def _pre_sigmoid(self,a,w):
        '''
        Compute the pre-sigmoid activation
        for a layer 
        '''
        z = np.zeros((a.shape[0],w.shape[1]))
        for i,te in enumerate(a):
            z[i] = (w.T * te).sum(1)
        return z
 
    def _sigmoid(self,la):
        '''
        compute the sigmoid function for an array
        of arbitrary shape and size
        '''
        return 1. / (1 + np.exp(-la))
 
    def activate(self,inp,params=None):
        '''
        Activate the net on a batch of training examples.
        return the input, and states of all layers for all
        examples.
        '''
 
        if None is params:
            params = self._netp
 
        # number of training examples
        m = inp.shape[0]
        # pre-sigmoid activation at the hidden layer
        z2 = self._pre_sigmoid(inp,params.w1) + np.tile(params.b1,(m,1))
        # sigmoid activation of the hidden layer
        a = self._sigmoid(z2)
        # pre-sigmoid activation of the output layer
        z3 = self._pre_sigmoid(a,params.w2) + np.tile(params.b2,(m,1))
        # sigmoid activation of the hidden layer
        o = self._sigmoid(z3)
 
        return inp,a,z2,z3,o
 
    ## PARAMETER LEARNING ################################################
 
    def _rcost(self,inp,params,a=None,z2=None,z3=None,o=None):
        '''
        The real-valued cost of using the parameters
        on a (batch) input
        '''
        if None == o:
            # activate the network with params
            ae = autoencoder(params)
            inp,a,z2,z3,o = ae.activate(inp,params=params)
        
 
        # find the norm of the difference between each
        # input/output pair
        diff = o - inp
        n = np.sqrt((diff**2).sum(1))
        
        # one half squared error between input and output
        se = (0.5 * (n ** 2)).sum()
        
        # cost is the average of the one half squared error
        c = ((1. / inp.shape[0]) * se)
 
        # sum of squared error + weight decay + sparse
        if self._include_weight_decay:
            c += self._weight_decay_cost(params=params)
 
        if self._include_sparsity:
            c += self._sparse_cost(a)
 
        return c
 
    def _fprime(self,a):
        '''
        first-derivative of the sigmoid function
        '''
        return a * (1. - a)
 
    def _sparse_ae_cost(self,inp,parms,check_grad = False):
        '''
        Get the batch error and gradients for many
        training examples at once and update
        weights and biases accordingly
        '''
 
        onem = (1. / len(inp))
 
        inp,a,z2,z3,o = self.activate(inp,params=parms)
        d3 = -(inp - o) * self._fprime(o)
        bp = self._backprop(d3,params=parms)
        spgd = np.zeros(bp.shape)
        if self._include_sparsity:
            spgd = self._sparse_grad(a)
            bp += spgd
        d2 = bp * self._fprime(a)
 
        wg2 = self._weight_grad(d3,a,parms.w2)
        wg1 = self._weight_grad(d2,inp,parms.w1)
 
        bg2 = self._bias_grad(d3)
        bg1 = self._bias_grad(d2)
        c = self._rcost(inp,parms,a=a,z2=z2,z3=z3,o=o)
        
        if check_grad:
 
            # unroll the gradients into a flat vector
            rg = params(self.indim,self.hdim,wg1,bg1,wg2,bg2).unroll()
 
            # perform a (very costly) numerical 
            # check of the gradients
            self._check_grad(parms,inp,rg)
 
        return c, wg2, wg1, bg2, bg1
 
    def _sparse_ae_cost_unrolled(self,inp,parms):
        c, wg2, wg1, bg2, bg1 = self._sparse_ae_cost(inp,parms)
        return params(self.indim,self.hdim,wg1,bg1,wg2,bg2).unroll()
 
    def _weight_decay_cost(self,params=None):
        if None is params:
            params = self._netp
 
        w1 = params.w1**2
        w2 = params.w2**2
        return (self._lambda / 2.) * (w1.sum() + w2.sum())
 
    def _sparse_cost(self,a):
        '''
        compute the sparsity penalty for a batch
        of activations.
        '''
        p = self._sparsity
        p_hat = np.average(a,0)
        a = p * np.log(p /p_hat)
        b = (1 - p) * np.log((1 - p) / (1 - p_hat))
        return self._beta * (a + b).sum()
 
 
    def _sparse_grad(self,a):
        p_hat = np.average(a,0)
        p = self._sparsity
 
        return self._beta * (-(p / p_hat) + ((1 - p) / (1 - p_hat)))
 
        
    def _bias_grad(self,cost):
        return (1. / cost.shape[0]) * cost.sum(0)
 
    def _weight_grad(self,cost,a,w):
        # compute the outer product of the error and the activations
        # for each training example, and sum them together to
        # obtain the update for each weight
        wg = (cost[:,:,np.newaxis] * a[:,np.newaxis,:]).sum(0).T
        wg = ((1. / cost.shape[0]) * wg)
        if self._include_weight_decay:
            wg += (self._lambda * w)
        return wg
 
    def _backprop(self,out_err,params=None):
        '''
        Compute the error of the hidden layer
        by performing backpropagation.
 
        out_err is the error of the output
        layer for every training example.
        rows are errors.
        '''
        if None is params:
            params = self._netp
        # the dot product of the layer 2 weights with output
        # error for each training example
        tiled = np.tile(params.w2[np.newaxis,:,:],(out_err.shape[0],1,1))
        return (tiled * out_err[:,np.newaxis,:]).sum(2)
 
 
    def _update(self,inp,wg2,wg1,bg2,bg1):
        if self._include_weight_decay:
            wg2 += self._netp.w2 * self._lambda
            wg1 += self._netp.w1 * self._lambda
 
        self._netp.w2 -= self._alpha * wg2
        self._netp.w1 -= self._alpha * wg1
        self._netp.b2 -= self._alpha * bg2
        self._netp.b1 -= self._alpha * bg1
 
        
 
    def _check_grad(self,params,inp,grad,epsilon = 10**-4):
 
        def rcst(x):
            return self._rcost(inp,params.roll(x,self.indim,self.hdim))
 
        def rcstprime(x):
            return self._sparse_ae_cost_unrolled(inp,params.roll(x,self.indim,self.hdim))
 
        err = check_grad(rcst,rcstprime,params.unroll())
 
        
        rc = self._rcost
        e = epsilon
        tolerance = e ** 2
        
        theta = params.unroll()
        num_grad = np.zeros(theta.shape)
 
 
        # compute the numerical gradient of the function by
        # varying the parameters one by one.
        for i in range(len(theta)):
            plus = np.copy(theta)
            minus = np.copy(theta)
            plus[i] += e
            minus[i] -= e
            pp = params.roll(plus,self.indim,self.hdim)
            mp = params.roll(minus,self.indim,self.hdim)
            num_grad[i] =  (rc(inp,pp) - rc(inp,mp)) / (2. * e)
 
        # the analytical gradient
        agp = params.roll(grad,self.indim,self.hdim)
        # the numerical gradient
        ngp = params.roll(num_grad,self.indim,self.hdim)
 
        diff = np.linalg.norm(num_grad - grad) / np.linalg.norm(num_grad + grad)
        # layer 1 weights difference
        print np.linalg.norm(ngp.w1 - agp.w1) / np.linalg.norm(ngp.w1 + agp.w1)
        # layer 2 weights difference
        print np.linalg.norm(ngp.w2 - agp.w2) / np.linalg.norm(ngp.w2 + agp.w2)
        # layer 1 bias difference
        print np.linalg.norm(ngp.b1 - agp.b1) / np.linalg.norm(ngp.b1 + agp.b1)
        # layer 2 bias difference
        print np.linalg.norm(ngp.b2 - agp.b2) / np.linalg.norm(ngp.b2 + agp.b2)
        print 'Difference between analytical and numerical gradients is %s' % str(diff)
        print 'scipy.optimize error is %s' % str(err)
        print '2norm is %s' % str(np.linalg.norm(num_grad - grad))
        print np.all(np.sign(num_grad) == np.sign(grad))
        #print diff < tolerance
        print '================================================================'
        print ngp.w1.max()
        print agp.w1.max()
        print ngp.w2.max()
        print agp.w2.max()
 
        '''
        plt.gray()
        plt.figure()
        # plot the analytical gradients on
        # the first row
        plt.subplot(2,4,1)
        plt.imshow(agp.w1)
        plt.subplot(2,4,2)
        plt.imshow(agp.w2)
        plt.subplot(2,4,3)
        plt.plot(agp.b1)
        plt.subplot(2,4,4)
        plt.plot(agp.b2)
        # plot the numerical (brute force)
        # gradients on the second row
        plt.subplot(2,4,5)
        plt.imshow(ngp.w1)
        plt.subplot(2,4,6)
        plt.imshow(ngp.w2)
        plt.subplot(2,4,7)
        plt.plot(ngp.b1)
        plt.subplot(2,4,8)
        plt.plot(ngp.b2)
        plt.show()
        '''
        return ngp.unroll()
        
    @property
    def indim(self):
        return self._netp._indim
 
    @property
    def hdim(self):
        return self._netp._hdim
 
 
    def train(self,inp,iterations,with_bfgs = False,grad_check_freq = None):
        
 
        def rcst(x):
            v = self._rcost(inp,params.roll(x,self.indim,self.hdim))
            print 'rcst says: %s' % str(v)
            return v
 
        def rcstprime(x):
            return self._sparse_ae_cost_unrolled(inp,params.roll(x,self.indim,self.hdim))
 
 
        if with_bfgs:
            x0 = self._netp.unroll()
            mn,val,d = bfgs(rcst,
                            x0,
                            fprime = rcstprime,
                            factr=100,
                            maxfun=800,
                            disp=1)
            print val
            print d['task']
            print d['warnflag']
            print d['grad'].sum()
            print d['funcalls']
            with open('autoencoder2.dat','wb') as f:
                cPickle.dump(mn,f)
            return mn
        else:
            for i in range(iterations):
                if grad_check_freq:
                    gc = i and not i % grad_check_freq
                else:
                    gc = False
                grads = self._sparse_ae_cost(inp,self._netp, check_grad = gc)
                # leave out cost, the first item
                # in the grads tuple
                self._update(inp,*grads[1:])
            return self._netp.unroll()
 
            
import argparse
import PIL
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Attempted autoencoder implementation')
    # You can download a zip file containing the images data and 
    # starter octave code from here: 
    # http://ufldl.stanford.edu/wiki/resources/sparseae_exercise.zip
    parser.add_argument('--imgpath',
                        help='path to IMAGES.mat')
    parser.add_argument('--usebfgs',
                        help='use scipy.optimize.fmin_l_bfgs_b to minimize cost',
                        action='store_true',
                        default=False)
    parser.add_argument('--nsamples',
                        help='number of patches to draw from images',
                        type=int,
                        default=10)
    parser.add_argument('--sparse',
                        help='include the sparsity term',
                        action='store_true',
                        default=False)
    parser.add_argument('--wd',
                        help='include the weight decay term',
                        action='store_true',
                        default=False)
 
 
    args = parser.parse_args()
 
    # size of input and output layers
    n_dim = 64
    # size of hidden layer
    h_dim = 25
 
    def random_image_patches(n_samples=args.nsamples):
        a = loadmat(args.imgpath)
        m = a['IMAGES']
        patches = np.zeros((n_samples,64))
        ri = np.random.randint
        for i in range(n_samples):
            img = ri(0,10)
            r = ri(0,504)
            c = ri(0,504)
            patches[i] = m[r:r+8,c:c+8,ri(0,10)].reshape(64)
        return patches
 
    # preprocess the data
    def preprocess(data):
        data -= data.mean(axis=0)
        pstd = 3 * data.std()
        data = np.maximum(np.minimum(data,pstd),-pstd) / pstd
        data = (data + 1) * .4 + .1
        return data
 
    samples = random_image_patches()
    samples = preprocess(samples)
 
    # if we're not using bfgs, do a numerical gradient check every
    # 10 training epochs
    gcf = 10 if not args.usebfgs else None
    #gcf = None
    # train the autoencoder
    ae = autoencoder(params(n_dim,h_dim),
                     include_weight_decay = args.wd,
                     include_sparsity = args.sparse)
    theta = ae.train(samples,                  # image patches
                     10000,                    # n epochs
                     with_bfgs = args.usebfgs, # use scipy.optimize.l_fmin_bfgs_b
                     grad_check_freq = gcf)    # perform a numerical gradient check every n iterations
    
 
    # plot the filters learned by the autoencoder
    with open('autoencoder2.dat','rb') as f:
        theta = cPickle.load(f)
    p = params.roll(theta,64,25)
    w1 = p.w1.T
    spacing = 1
    img = np.ones((8 * 5 + 8,8 * 5 + 8))
    fn = 0
    for i in range(5):
        for q in range(5):
            x = i * (8 + 1) + 1
            y = q * (8 + 1) + 1
            img[x:x+8,y:y+8] = w1[fn].reshape((8,8))
            fn +=1
 
    img *= 255. / img.max()
    image = PIL.Image.fromarray(img)
    image = image.convert('L')
    image.save('filters.bmp')
 
 
    '''
    # grab some new patches and reconstruct them
    num_plots = 10
    samples = random_image_patches(num_plots)
    samples = preprocess(samples)
    plt.figure()
    for i in range(num_plots):
        signal = samples[i]
        inp,a,z2,z3,o = ae.activate(np.array([signal]))
        plt.subplot(num_plots,1,i + 1)
        plt.plot(signal,'b-')
        plt.plot(o[0],'g-')
    plt.show()
    '''