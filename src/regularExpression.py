import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*?)than(.*).*' ,line, re.M|re.I)

if matchObj:

                    print(matchObj.group())
                    print(matchObj.group(1))
                    print(matchObj.group(2))

else:
                    print("No match")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
