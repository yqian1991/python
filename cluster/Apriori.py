def loadDataSet():
  return [ [1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataset):
  C1 = []
  for transaction in dataset:
    for item in transaction:
      if not [item] in C1:
        C1.append([item])
  C1.sort()
  print C1
  return map(frozenset, C1)

def scanD(D, Ck, minSupport):
  ssCnt = {}
  for tid in D:
    for can in Ck:
      if can.issubset(tid):
        if not ssCnt.has_key(can): ssCnt[can] = 1
        else: ssCnt[can] += 1
  numItems = float(len(D))
  retlist = []
  supportData = {}
  for key in ssCnt:
    support = ssCnt[key]/numItems
    if support >= minSupport:
      retlist.insert(0, key)
    supportData[key] = support
  return retlist, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()                           
            if L1==L2:                                   
                retList.append(Lk[i] | Lk[j]) 
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)     
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

if __name__ == "__main__":
  dataset = loadDataSet()
  C1 = createC1(dataset)
  print C1
  D = map(set, dataset)
  L1, suppData0 = scanD(D, C1, 0.5)
  L,suppData = apriori(dataset)
  aprioriGen(L[0], 2)
  L,suppData = apriori(dataset,minSupport=0.7)
  print L