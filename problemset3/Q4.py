'''
Name:Q4.py
Description:program to print a word that have no e and percentage of word that have no e
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


#function to print a word that have no e and percentage of word that have no e
def test_function(mylist):
  count=0
  #length of a word in a list
  length_word=len(mylist)
  percentagecount=0
  for i in mylist:
    mylist1=list(i)
    for j in mylist1:
      if j=='e':
        count+=1
        break
    if(count!=1):
      percentagecount+=1
      #printing a word that have no e
      print("a word that have no e in a list:  "+i)
    mlist1=[]
    count=0
  #calculating percentage of word
  percentage_word=(float(percentagecount)/float(length_word))*100
  print("percentage of the word that have no e:"+str(int(percentage_word))+"%")
  
        


mylist=[]
input=int(raw_input("enter a number to insert a word into the list"))
for i in range(0,input):
  string=raw_input("enter string:")
  mylist.append(string)
test_function(mylist)