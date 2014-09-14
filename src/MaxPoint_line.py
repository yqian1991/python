#[(0,-12),(5,2),(2,5),(0,-5),(1,5),(2,-2),(5,-4),(3,4),(-2,4),(-1,4),(0,-5),(0,-8),(-2,-1),(0,-11),(0,-9)]

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        sizel = len(points)
        if sizel<=2:
            return sizel
        
        dict2 = {}
        for i in range(0, sizel):
            key=(points[i].x ,points[i].y)
            if key in dict2:
                dict2[key] += 1
            else:
                dict2[key] = 1
        print len(dict2)
        
        size = len(dict2)
        if size<=2:
            return sizel
           
        p = dict2.keys()
        #print p
        i=0
        num=0
        for i in range (0, size-1):
            dict1={}
            for j in range(i+1, size):
                if p[j][0]-p[i][0] == 0:
                    rate=str(p[i][0])
                    #rate = 1000000
                else:
                    rate = (float)(p[j][1]-p[i][1])/(float)(p[j][0]-p[i][0])
                #print rate
                if rate in dict1:
                    if p[i] not in dict1[rate]: 
                        dict1[rate].append(p[i])
                    if p[j] not in dict1[rate]:
                        dict1[rate].append(p[j])
                        #print dict1[rate]
                else:
                    nl=[p[i],p[j]]
                    dict1[rate] = nl
            print p[i][0], p[i][1], dict1
            numlist=[]
            for (k,v) in dict1.items():
				#print k,v
				c=0
				for kk in v:
					c += dict2[kk]
				numlist.append(c)

            newnl = sorted(numlist, reverse=True)
            print newnl[0]
            if num<newnl[0]:
				num = newnl[0]	

        return num
        

if __name__ =='__main__':
	'''
    p = Point(0,-12)
    p1 = Point(5,2)
    p2 = Point(2,5)
    p3 = Point(0,-5)
    p4 = Point(1,5)

    p5 = Point(2,-2)
    p6 = Point(5,-4)
    p7 = Point(3,4)
    p8 = Point(-2,4)
    p9 = Point(-1,4)

    p10 = Point(0,-5)
    p11 = Point(0,-8)
    p12 = Point(-2,-1)
    p13 = Point(0,-11)
    p14 = Point(0,-9)

    l=[]
    l.append(p)
    l.append(p1)
    l.append(p2)
    l.append(p3)
    l.append(p4)
    l.append(p5)
    l.append(p6)
    l.append(p7)
    l.append(p8)
    l.append(p9)
    l.append(p10)
    l.append(p11)
    l.append(p12)
    l.append(p13)
    l.append(p14)
	'''
	p = Point(0,0)
	p1 = Point(1,1)
	p2 = Point(1,-1)
	l=[]
	l.append(p)
	l.append(p1)
	l.append(p2)
	sol = Solution()
	print sol.maxPoints(l)