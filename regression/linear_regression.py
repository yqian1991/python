from numpy import *
import matplotlib.pyplot as plt 
import sys

def loadDataSet(fileName):
  #numFeat: number of columns
  numFeat = len(open(fileName).readline().split('\t')) - 1
  dataMat = []; labelMat = []
  fr = open(fileName)
  for line in fr.readlines():
    lineArr = []
    curLine = line.strip().split('\t')
    for i in range(numFeat):
      lineArr.append(float(curLine[i]))
    dataMat.append(lineArr)
    labelMat.append(float(curLine[-1]))
  return dataMat, labelMat

def standRegress(xArr, yArr):
  xMat = mat(xArr); yMat = mat(yArr).T
  xTx = xMat.T*xMat
  if linalg.det(xTx) == 0.0:
    print "Singular matrix, can not inverse"
    return
  ws = xTx.I * (xMat.T*yMat)
  return ws

def standRegressTest():
  xArr, yArr = loadDataSet('ex0.txt')
  print len(xArr), len(yArr)

  ws = standRegres(xArr, yArr)
  print ws
  xMat = mat(xArr)
  yMat = mat(yArr)
  yHat = xMat * ws
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
  xCopy = xMat.copy()
  xCopy.sort(0)
  yHat = xCopy * ws
  sys.setrecursionlimit(30000)
  #print ax.plot(xCopy[:,1], yHat)
  plt.show()

  #Get correlation
  yHat = xMat * ws
  print corrcoef(yHat.T, yMat)

def lwlr(testPoint, xArr, yArr, k=1.0):
  xMat = mat(xArr); yMat = mat(yArr).T
  m = shape(xMat)[0]
  weights = mat(eye(m))
  for j in range(m):
    diffMat = testPoint - xMat[j,:]
    weights[j,j] = exp(diffMat * diffMat.T/(-2.0*k**2))
  xTx = xMat.T * (weights * xMat)
  if linalg.det(xTx) == 0.0:
    print "This matrix is Singular, cannot inverse"
    return
  ws = xTx.I * (xMat.T * (weights*yMat))
  return testPoint*ws

def lwlrTest( ):
  k = 1.0
  xArr, yArr = loadDataSet("ex0.txt")
  testArr = xArr
  m = shape(testArr)[0]
  yHat = zeros(m)
  for i in range(m):
    yHat[i] = lwlr(testArr[i], xArr, yArr, k)
  xMat = mat(xArr)
  srtInd = xMat[:,1].argsort(0)
  xSort = xMat[srtInd][:, 0, :]
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(xSort[:,1], yHat[srtInd])
  ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
  plt.show()

def stageWise(xArr, yArr, eps=0.01, numIt=100):
  xMat = mat(xArr); yMat = mat(yArr).T
  yMean = mean(yMat, 0)
  yMat = yMat - yMean
  xMat = regularize(xMat)
  m, n = shape(xMat)
  ws = zeros((n, 1)); wsTest = ws.copy(); wsMax = ws.copy()
  for i in range(numIt):
    print ws.T
    lowestError = inf;
    for j in range(n):
      for sign in [-1, 1]:
        wsTest = ws.copy()
        wsTest[j] += eps.sign
        yTest = xMat*wsTest
        rssE = rssError(yMat.A, yTest.A)
        if rssE < lowestError:
          lowestError = rssE
          wsMax = wsTest
    ws = wsMax.copy()
    returnMat[i,:] = ws.T
  return returnMat

def stageWiseTest():
  xArr, yArr = loadDataSet('ex0.txt')
  return stageWise(xArr, yArr, 0.01, 200)

def rssError(yArr, yHatArr):
  return ((yArr-yHatArr)**2).sum()

if __name__ == "__main__":
  #standRegresTest()
  #lwlrTest()
  print stageWiseTest()

   
