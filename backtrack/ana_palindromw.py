def solution(file_object):
    #result = []
    for line in file_object.readlines():
        if isValidInteger(line):
            #result.append(int(line))
            yield int(line)
            
    #return result

def isValidInteger(line):
    try: 
        value = int(line)
        #print value
        if value <= 1000000000 and value >= -1000000000:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__=="__main__":
	f = open("/home/yu/test.txt", "r")
	#solution(f)
	for i in solution(f):
		print i

