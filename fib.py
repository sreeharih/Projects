# -*- di gut-8 -*-i 
"""
fibonacci series
by Sreehari
"""
#fibonacci
s=0
s1=1
num=int(input("How many terms of the series do you want:"))
print(s,end=",")
for i in range(1,num):
    sum=s+s1
    if i!=num-1:
        print(s1,end=",")    
    else:
        print(s1,end=".")    
    s=s1
    s1=sum
    