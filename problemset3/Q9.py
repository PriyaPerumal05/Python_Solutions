'''
Name:Q9.py
Description:program to check if the list is sorted in ascending order 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check if the list is sorted in ascending order 
def is_sorted(mylist):
  word=sorted(mylist)
  #comparing sorted list and original list
  if mylist==word:
    return True
  else:
    return False
  
  
#getting input from user  
string=raw_input("enter word:")
#converting string to a list
mylist=list(string)
result=is_sorted(mylist)
print(result)