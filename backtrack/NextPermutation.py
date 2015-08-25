class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def getPermutation(self, n, k):
        ll = [str(i) for i in range(1, n+1)] #means all groups
        #groups 1: 1xxxxxx
        #groups 2: 2xxxxxx
        #...
        #groups n: nxxxxxx

        divisor = 1
        for i in range(1, n):
        	divisor *= i #divisor is all elements in a group

        answer = ""
        while k>0 and k<=divisor*n:
            #every group has divisor numbers
            group_number = k/divisor
            k %= divisor 
            if k>0:#result is the kth number of group_num+1 group
                choose = ll.pop(group_number) # the first digit
                answer += choose
            else:
            	choose = ll.pop(group_number - 1)
            	answer += choose
            	ll.reverse()
            	answer += "".join(ll)
            	break

            divisor /= len(ll) # update the number of elements 
        return answer 
			
			
if __name__=="__main__":
	sol = Solution()
	print sol.getPermutation(6, 100)
