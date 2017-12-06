'''
Name: Q1.py
Description:program to find whether string is a palindrome or not
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


#function definition to find whether string is a palindrome or not
def is_palindrome(string):
  if len(string)<=2 and string[0]==string[-1]:
    print 'It is a Palindrome'
  elif string[0]==string[-1]:
    #recursive call
    is_palindrome(string[1:-1])
  else:
     print 'It is not a Palindrome'
 
#getting input from user    
string=raw_input("enter string:")
#function call for palindrome
is_palindrome(string)
