'''
Name:Q3.py
Description:program to check whether a word contain a letter e 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check whether a word contain a letter e 
def has_no_e(word):
  if 'e' in word:
    return "False"
  elif 'E' in word:
	  return "False"
  else:
    return "True"

#getting input from user
word=raw_input("enter word")
#function call
result=has_no_e(word)
print(result)

