class Solution:
    # @return a string
    def countAndSay(self, n):
		if n==0:
			return ""
		if n==1:
			return "1"
		if n==2:
			return "11"
		strs = "11"
		iters = n-2
		
		res=""
		while iters>0:	
			#prev=strs[0]
			dicts={strs[0]:1}
			num = 1
			res=""
			while num <= len(strs):
				if num == len(strs):
				  	key, value = dicts.popitem()
					res += str(value)+str(key)
				else:
					cur = dicts.iterkeys().next()
					ch = strs[num]
					if ch!=cur:
						key, value = dicts.popitem()
						dicts={ch:1}
						res += str(value)+str(key)
						#print res
					elif ch == cur:
						dicts[cur] += 1
						#print dicts
				num  = num + 1
			#print res
			strs = res
			iters = iters - 1
		return res
						

if __name__=="__main__":
	sol = Solution()
	print sol.countAndSay(5)
