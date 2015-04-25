from numpy import *

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
