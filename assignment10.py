#Que1
f=open("que1.txt",'r')
"""open is used to open the file in r mode i.e. read mode"""
data=f.read()
"""read reads the content of file"""
print(data)
f.close()
"""close closes the file"""
print()

#Que2
f=open("que2.txt",'r')
data=f.read()
words=data.split()
dict={}
for word in words:
    dict[word]=words.count(word)
print(dict)
f.close()
print()

#Que3
f=open("que1.txt",'r')
line=f.readlines()    
for l in line:
    f1=open("que3.txt",'a')
    f1.write(l)
    f1.close()
f.close()
print()

#Que4
f=open("que1.txt",'r')
f1=open("que3.txt",'r')
for l1,l2 in zip(f,f1):
    f2=open("que4.txt",'a')
    f2.write(l1+l2)
    f2.close()
f.close()
f1.close()
print()

#Question 5
import random as r
f=open("file1.txt",'w')
for i in range(10):
    a=r.randint(1,9)
    f.write(str(a)+"\n")
f.close() 
f=open("file1.txt","r")
a=f.readlines()
a.sort()
f.close()
f=open("file2.txt",'w')
for i in range(len(a)):
    f.write(a[i])
f.close()
       
