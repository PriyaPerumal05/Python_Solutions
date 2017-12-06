'''
Name:Q6.py
Description:program to print the number of words that don't contain any of the forbidden letters
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:06/12/2017
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
    
#getting string of forbidden letters
forbidden=raw_input("enter forbidden word")
mylist=list(forbidden)
pr=0
for i in range(0,5):
  #getting input from user
  word=raw_input("enter word")
  result=avoids(word,mylist)
  if(result=="True"):
    pr+=1
print("print the no of words that don't contain forbidden letters:"+str(pr))

