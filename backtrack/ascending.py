import random
def solution(A):
    # write your code in Python 2.7
	result = []
	max_counter = 0 # save the slice with largest length
	counter = 0 #the length of a valid slice
	start_pos = 0 # the start index of each slice
	
	for i in range(0, len(A)):
		if i == 0:
			counter = 1
			start_pos = i

		if i > 0:
			current = A[i]
			previous = A[i-1]

			if current <= previous:
				counter = 1
				start_pos = i
			if current > previous:
				counter += 1
				
		if counter > max_counter:
			result = []

		max_counter = max(counter, max_counter)

		if counter == max_counter:
			result.append(start_pos)
			
	#return random beginning of slices
	return random.choice(result)

def solution2(A):
    if len(A) > 0:
        average = sum(A)*1.0/len(A)
        max_deviation = 0
        pos = 0            
        for i in range(len(A)):
            if abs(A[i] - average) > max_deviation:
                max_deviation = abs(A[i] - average)
                pos = i
        return pos
    else:
        return -1

def solution3(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2 
        if A[m] >= X:
            r = m - 1
        else:
            l = m + 1
    if A[l] == X:
        return l
    return -1
    
if __name__=="__main__":
	print solution([100, 2, 5, 9, 9, 10, 10, 10, 11])
