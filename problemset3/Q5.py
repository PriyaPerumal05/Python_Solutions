'''
Name:Q5.py
Description:program to check whether a word contain a string of forbidden letters 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check whether a word contain a string of forbidden letters
def avoids(word,mylist):
  count=0
  for i in mylist:
    if i in word:
      count=0
      break
    else:
      count+=1
  if(count>0):
    return "True"
  else:
    return "False"

#getting input from user
word=raw_input("enter word")
#getting string of forbidden letters
forbidden=raw_input("enter forbidden word")
mylist=list(forbidden)
result=avoids(word,mylist)
print(result)



