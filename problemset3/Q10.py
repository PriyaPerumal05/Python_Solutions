'''
Name:Q10.py
Description:program to check whether it is a anagram 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check whether it is a anagram
def is_anagram(x1,y1):
  leng_x=len(x1)
  leng_y=len(y1)
  if leng_x==leng_y:
    x1.sort()
    y1.sort()
    if x1==y1:
      return "True"
    else:
      return "False"
  else:
    return "False"


#getting input from user
x=raw_input("enter word1:")
y=raw_input("enter word2:")
#converting word to a list
x1=list(x)
y1=list(y)
result=is_anagram(x1,y1) 
print(result)




