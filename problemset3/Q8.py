'''
Name:Q8.py
Description:program to check whether the word is sorted or not
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to check whether the word is sorted or not
def is_abecedarian(word):
  i=0
  while i<len(word)-1:
    if word[i+1]<word[i]:
      return False
    i=i+1
  return True

#getting from user
word=raw_input("enter the string:")
string=is_abecedarian(word)
print("sorted string or not:"+str(string))




