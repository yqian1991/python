###########################
#kNN: k Nearest Neighbors

#Input: newInput: vector to compare to existing dataset
#       dataSet : size m data set of known vectors
#       lables  : data set labels
#       k       : number of neighbors to use for comparison

#Output:  the most popular class label
############################

from numpy import *
import operator
import os

def createDataSet():
	group = array([ [1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
	labels = ['A', 'A', 'B', 'B']

	print "Group:\n",group
	print "Labels:", labels
	return group, labels

def kNNClassify(newInput, dataSet, labels, k):
	numSamples = dataSet.shape[0] #shape[] stands for the num of row
	#print "numSamples:",numSamples

	##step 1: calculate Eucliden distance
	#tile(A, reps): construct an array by repeating A reps times
	#the following copy numSamples row for dataset
	newTile = tile(newInput, (numSamples ,1))
	#print "Tile:", newTile

	diff = newTile - dataSet
	#print "Diff:", diff
	squaredDiff = diff ** 2
	#print "squaredDiff:", squaredDiff
	squaredDist = sum(squaredDiff, axis = 1)
	#print "squaredDist:", squaredDist
	distance = squaredDist ** 0.5
	#print "Distance:", distance

	##step 2: sort the distance
	#argsort() returns the indices that would sort an array in a ascending order
	sortedDistIndices = argsort(distance)
	#print "sortedDistIndices:", sortedDistIndices

	classCount = {} #define a dictionary
	for i in xrange(k):
		##step 3: choose the min k distance
		voteLabel = labels[sortedDistIndices[i]]

		##step 4: count the times labels occur
		#when the key voteLabel is not in the dictionary classCount, get()
		#will return 0
		classCount[voteLabel] = classCount.get(voteLabel, 0)+1
	
	##step 5: the max voted class will return
	maxCount = 0
	for key, value in classCount.items():
		if value > maxCount:
			maxCount = value
			maxIndex = key

	return maxIndex

def img2vector(filename):
	rows = 32
	cols = 32
	imgVector = zeros((1, rows * cols))
	fileIn = open(filename)
	for row in xrange(rows):
		lineStr = fileIn.readline()
		for col in xrange(cols):
			imgVector[0, row * 32 + col] = int(lineStr[col])
	
	return imgVector
# load dataSet
def loadDataSet():
	## step 1: Getting training set
	print "---Getting training set..."
	dataSetDir = 'C:/Users/Administrator/Downloads/'
	trainingFileList = os.listdir(dataSetDir + 'trainingDigits') # load the training set
	numSamples = len(trainingFileList)

	train_x = zeros((numSamples, 1024))
	train_y = []
	for i in xrange(numSamples):
		filename = trainingFileList[i]

		# get train_x
		train_x[i, :] = img2vector(dataSetDir + 'trainingDigits/%s' % filename) 

		# get label from file name such as "1_18.txt"
		label = int(filename.split('_')[0]) # return 1
		train_y.append(label)

	## step 2: Getting testing set
	print "---Getting testing set..."
	testingFileList = os.listdir(dataSetDir + 'testDigits') # load the testing set
	numSamples = len(testingFileList)
	test_x = zeros((numSamples, 1024))
	test_y = []
	for i in xrange(numSamples):
		filename = testingFileList[i]

		# get train_x
		test_x[i, :] = img2vector(dataSetDir + 'testDigits/%s' % filename) 

		# get label from file name such as "1_18.txt"
		label = int(filename.split('_')[0]) # return 1
		test_y.append(label)

	return train_x, train_y, test_x, test_y

# test hand writing class
def testHandWritingClass():
	## step 1: load data
	print "step 1: load data..."
	train_x, train_y, test_x, test_y = loadDataSet()

	## step 2: training...
	print "step 2: training..."
	pass

	## step 3: testing
	print "step 3: testing..."
	numTestSamples = test_x.shape[0]
	matchCount = 0
	for i in xrange(numTestSamples):
		predict = kNNClassify(test_x[i], train_x, train_y, 3)
		print "predict:", predict 
		print "value:", test_y[i]
		if predict == test_y[i]:
			matchCount += 1
		else:
			print "predict:", predict 
			print "value:", test_y[i]

	accuracy = float(matchCount) / numTestSamples

	## step 4: show the result
	print "step 4: show the result..."
	print 'The classify accuracy is: %.2f%%' % (accuracy * 100)

if __name__ == '__main__':
	import kNN
	from numpy import *

	dataSet, labels = kNN.createDataSet()

	testX = array([0.2, 0.01])
	k = 3
	outputLabel = kNN.kNNClassify(testX, dataSet, labels, 3)
	print "Your input is", testX, "and classified to class:", outputLabel

	kNN.testHandWritingClass()