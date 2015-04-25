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

def standRegres(xArr, yArr):
  xMat = mat(xArr); yMat = mat(yArr).T
  xTx = xMat.T*xMat
  if linalg.det(xTx) == 0.0:
    print "Singular matrix, can not inverse"
    return
  ws = xTx.I * (xMat.T*yMat)
  return ws

if __name__ == "__main__":
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
