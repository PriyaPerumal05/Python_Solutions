'''
Name:Q2.py
Description:program to rotate a word using the given input 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

#function to rotate a word using the given input 
def rotate_word(num,string):
  result=''
  for i in string:
    str=ord(i)+num
    if((str>=97 and str<=122) or (str>=65 and str<=90)):
      result=result+(chr(str)) 
    elif(str<97 or str<65):
      str=str+26
      result=result+(chr(str))
    elif(str>122 or str>90):
      str=str-26
      result=result+(chr(str))
  print(result)

  
#getting input from user
num=int(raw_input("enter no to be rotated"))
string=raw_input("enter string")
rotate_word(num,string)

