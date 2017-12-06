'''
Name:Q7.py
Description:program to check whether the word containing only letters in the list
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check whether the word contains only letters in the list
def using_only(word,string):
  for i in word: 
    if i not in string:
      return False
  return True

#getting input from user
word=raw_input("enter string:")
string=list(raw_input("enter string"))
result=using_only(word,string)
print(result)
 


