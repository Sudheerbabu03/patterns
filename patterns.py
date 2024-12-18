'''n=int(input())
for i in range(1,n+1):
    print('* '*i)

*
* *
* * *
* * * *
* * * * *


n=int(input())
for i in range(1,n+1):
    print('  '*(n-i)+'* '*i)

 

        *
      * *
    * * *
  * * * *
* * * * *



n=int(input())
for i in range(n):
    print('* '*(n-i))

* * * * *
* * * *
* * *
* *
*



n=int(input())
for i in range(n):
    print('  '*i+'* '*(n-i))


* * * * *
  * * * *
    * * *
      * *
        *    

  


n=int(input())
for i in range(n):
    print(' '*i+'* '*(n-i))


* * * * *
 * * * *
  * * *
   * *
    *


n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)

    *
   * *
  * * *
 * * * *
* * * * * 



n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()    
   

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()    

         1
       1 2
     1 2 3
   1 2 3 4
 1 2 3 4 5
        
 

n=int(input())
for i in range(1,n+1):
    # print('  '*())
    for j in range(i,n+1):
        print(j,end=' ')
    print()    
        
     
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5     



n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()    


5 4 3 2 1
4 3 2 1
3 2 1
2 1
1    
       


# n=int(input())
# for row in range(1,n+1):
#     print(' '*row+'*')


# n=int(input())
# for row in range(1,n+1):
#     print(' '*(n-row)+'*')


# n=int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==col:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()           
        

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i!=j:
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()            


# n=5
# for i in range(1,n+1):
#     print('* '*i)

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print('*',end=' ')
    print()

      or

* 
* *
* * *
* * * *
* * * * *


# n=5
# for i in range(1,n+1):
#     print('  '*(n-i)+'* '*i)


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ') 
    print()           



        * 
      * *
    * * *
  * * * *
* * * * *



# n=5
# for i in range(1,n+1):
#     print('  '*i+'* '*(n+1-i))

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()            

* * * * * 
  * * * *
    * * *
      * *
        *



n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=5
for i in range(1,n+1):
    print('* '*(n+1-i)+'  '*i)

* * * * *   
* * * *
* * *
* *
*



n=5
stars=1
spaces=n-1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end='')
    print() 
    spaces-=1      



        *
      *
    *
  *
*  



n=5
stars=1
spaces=n-1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1

        * 
      * *
    * * *
  * * * *
* * * * *     



n=5
spaces=0
stars=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1

* 
* *
* * *
* * * *
* * * * *   


n=5
spaces=0
stars=n
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars-=1        

* * * * * 
* * * *
* * *
* *
*    

'''

'''

n=5
stars=1
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1

n=5
stars=1
spaces=n-1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1


n=5
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1    


'''
# n = 5
# stars = 1
# spaces = n+1

# for i in range(1, n + 1):
#     # Print spaces
#     for j in range(1,spaces//2+1):
#         print(' '*j, end=' ')
#     # Print stars
#     for k in range(stars):
#         print('* ', end=' ')
    
#     print()  # Move to the next line
#     spaces-=1
#     stars += 1
'''
n= 5
stars = 1
spaces = n  # Initialize the number of spaces to n

for i in range(1, n + 1):
    # Print spaces
    for j in range(spaces):
        print(' ', end='')
    # Print stars
    for k in range(stars):
        print('*', end=' ')
    
    print()  # Move to the next line
    spaces -= 1  # Decrease spaces for the next row
    stars += 1  # Increase stars for the next row



'''
'''
n=5 
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end='')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1        



n=5
num=1
m=1
spaces=0
for i in range(1,n+1):
    for j in  range(1,spaces+1):
        print(' ',end='')
    for k in range(m,num+1):
        print(k*1,end=' ') 
    print()
    spaces-=1
    num+=1      
'''
'''
n=3
stars=1
spaces=n
for i in range(1,n+1):
    for j in range(1,spaces):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2    

  '''          

'''
n=5
stars=1
spaces=n
for i in range(1,n+1):
    for j in range(1,spaces):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=2        



n=int(input('how many rows do you want'))
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+n):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2

n=int(input('how many rows do you want'))
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+n):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2

'''
'''

# n=int(input('how many rows do you want'))
# stars=
# spaces=0
# for i in range(1,n+1):
#     for j in range(1,spaces+1):
#         print(' ',end=' ')
#     for k in range(1,stars+1):
#         if 
#         print('*',end=' ')
#     print()
#     spaces-=1
#     stars-=2
''' 

'''
m=int(input())
stars=1  
spaces=m//2
for i in range(1,m+1):   
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1):
        print('*',end=' ')
            
    print()
    if i<=m//2:
        spaces-=1
        stars+=2
        
        
    else:
        stars-=2 
        spaces+=1
        


m=int(input())
stars=1  
spaces=0
for i in range(1,m+1):   
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+m):
        print('*',end=' ')
            
    print()
    if i<=m//2:
        spaces+=1
        stars-=2
        
        
    else:
        stars+=2 
        spaces-=1

        
        
'''
'''
n=5
num=n
spaces=0
for i in range(1,n+1):
    for k in range(1,spaces+1):
        print(' ',end=' ')
    for j in range(1,num+1):
        print(num,end=' ')
    print()
    spaces+=1
    num-=1    

'''

'''
1 2 3 4 5 
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25





n=5
num=1
spaces=0
for i in range(1,n+1):
    #for k in range(1,spaces+1):
        #print(' ',end=' ')
    for j in range(1,n+1):
        print(num,end='  ')
        num+=1
    print()
    spaces+=1
    # num-=1        




1 6 11 16 21 
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25

n=5

for i in range(1,n+1):
    num1=i
    #for k in range(1,spaces+1):
        #print(' ',end=' ')
    for j in range(1,n+1):
        print(i,end=' ')
        i+=5
        
    print()

    

1  2  3  4  5  
2  3  4  5  6
3  4  5  6  7
4  5  6  7  8
5  6  7  8  9
6  7  8  9  10





n=5

for i in range(1,n+2):
    num1=i
    #for k in range(1,spaces+1):
        #print(' ',end=' ')
    for j in range(1,n+1):
        print(i,end='  ')
        i+=1  
    print()
    
    

1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5




n=5
num=1
for i in range(1,n+1):
    for j in range(1,num+1):
        print(num,end=' ')
    print()
    num+=1   



1 
2 3
3 4 5


n=3
for i in range(1,n+1):
    num=i
    for j in range(1,num+1):
        print(num,end=' ')
        num+=1

    print()
   



1 2 3 4 5 
2 4 6 8 10
3 4 5 6 7
4 6 8 10 12
5 6 7 8 9

n=5
for i in range(1,n+1):
    num=i
    for j in range(1,n+1):
        print(num,end=' ')
        if i%2==0:
            num+=2  
        else:
            num+=1        

    print()





1 
2 3
3 4 5
4 5 6 7
5 6 7 8 9

n=5

for i in range(1,n+1):
    num=i
    for j in range(1,num+1):
        print(num,end=' ')
        num+=1
    print()
        



1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5



n=5
for i in range(1,n+1):
    num=i
    for j in range(1,num+1):
        print(j,end=' ')
        # num+=1    
    print()
    

    '''  
    
'''
n=5
for i in range(1,n+1):
    num=i
    for j in range(1,num+1):
        print(j,end=' ')
        num+=1
    print()    




       1 
     2 2 2 
   3 3 3 3 3 
 4 4 4 4 4 4 4 



n=4
spaces=n
num=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,num+i):
        print(num,end=' ')  
    print()
    spaces-=1
    num+=1      



        1 
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5





n=5
num=1
for i in range(1,n+1):
    print('  '*(n-i)+(str(i)+' ')*num)
    num+=2
    




     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5



n=5
num=1
spaces=n
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end='')
    for k in range(1,num+1):
        print(k,end=' ')
    print()
    spaces-=1
    num+=1        

      or
n=5
s=''
for i in range(1,n+1):
    s+=str(i)+' '
    print(' '*(n-i)+s)  

    





5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 



n=5
num=5
for i in range(1,n+1):
    for j in range(1,num+1):
        print(num,end=' ')
    print()
    num-=1    




1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1


n=int(input()) #9
num=1
for i in range(1,n+1):
    for j in range(1,num+1):
        print(num,end=' ')
    print()
    if i<=n//2:
        num+=1
    else:
        num-=1        


n=9
num=1
for i in range(1,n+1):
    print((str(num)+' ')*num)
    if i<=n//2:
        num+=1
    else:
        num-=1    

        
        

* * * * * 
+ + + + 
+ + + 
+ + 
+ 




n=5
stars=5
p=5
for i in range(1,n+1):
    if i>=2:
        for k in range(1,p+1):
            print('+',end=' ')
    else:
        for j in range(1,stars+1):
            print('*',end=' ')
    
    print()        
    p-=1



n=5
for i in range(1,n+1):
    if i>=2:
        print('+ '*(n+1-i))
    else:    
        print('* '*n)



* 
* * 
* * * 
* * * 
* * 
* 



n=5
stars=1
for i in range(1,n+1):
    for j in range(1,stars+1):
        print('*',end=' ')
        
    print()
    if i<=n//2:
        stars+=1
    else:
        print('*',end=' ')
        stars-=1

n=3
num=1
for i in range(1,n+1):
    print('* '*i)
for i in range(n,0,-1):
    print('* '*i)
 

        #
      + #
    + + #
  + + + #
+ + + + #
  + + + #
    + + #
      + #
        #


    

  
n=int(input())
for i in range(1,2*n):
    if(i==1):
        print('  '*(n-i)+'#')
    elif(i<=n):
        print('  '*(n-i)+'+ '*(i-1)+'#')
    else:
        print('  '*(i-n)+'+ '*(2*n-i-1)+'#')      
        


n=6
spaces=n-1
stars=0
spaces1=1
for i in range(1,2*n):
    for j in range(1,spaces+1):
        print(' ',end=' ')     
    if i<=n:
        print('+ '*(i-1)+'#')
        spaces-=1  
    else:
        for k in range(1,spaces1+1):
            print(' ',end=' ')
        print('+ '*(2*n-i-1)+'#') 
        spaces1+=1
           

        * 
      * * 
    *   * 
  *     * 
* * * * *   



n=5
for i in range(1,n+1):
    if i==1:
        print('  '*(n-i)+'* ')
    elif i==n:
        print('* '*i) 
    else:
        print('  '*(n-i)+'* '+'  '*(i-2)+'*')             



* 
* *
*   *
*     *
* * * * *


n=5
for i in range(1,n+1):
    if i==1:
        print('* ')
    elif i==n:
        print('* '*i) 
    else:
        print('* '+'  '*(i-2)+'*')


01 02 03 04 05 
02 04 06 08 10 
03 06 09 12 15 
04 08 12 16 20 
05 10 15 20 25
    

s='I Love Errors'
d={}
a='spaces'
b='vowels'
c='consonents'
for i in range(len(s)):
    if s[i]==' ':
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    elif s[i] in 'aeiouAEIOU':
        if b not in d:
            d[b]=1
        else:
            d[b]+=1            
    else:
        if s[i] not in 'aeiouAEIOU':
            if c not in d:
                d[c]=1
            else:
                d[c]+=1    



print(d)            
  
s='I Love Errors'
spaces=0
vowels=0
consonents=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        vowels+=1
    elif s[i]==' ':
        spaces+=1
    else:
        consonents+=1
print(f"spaces:{spaces}\nvowels:{vowels}\nconsonents:{consonents}")             
.l8.l/
                              



        1                                                                
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
o     n
n=5
spaces=n-1
stars=1
for i in range(1,n+1):
    d=i
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(1,stars+1): 
        print(d,end=' ')
        if k<=stars//2:
            d-=1
        else:
            d+=1       
    print()
    spaces-=1
    stars+=2              





5 5 5 5 5
5 4 4 4 4
5 4 3 3 3
5 4 3 2 2
5 4 3 2 1



n=50
for i in range(1,n+1):
    num=5

    for j in range(1,n+1):
        print((num),end=' ')
        if i>j:
            num-=1


    print()    



#alphabets

        A 
      A B
    A B C
  A B C D
A B C D E




n=5
num=1
spaces=n-1
for i in range(1,n+1):
    a=65
    for k in range(1,spaces+1):
        print(' ',end=' ')
    for j in range(1,num+1):
        print(chr(a),end=' ')
        a+=1
    print()
    num+=1 
    spaces-=1   


A 
B B
C C C
D D D D
E E E E E




A 
A B
A B C
A B C D
A B C D E




n=5
num=1
#spaces=n-1
for i in range(1,n+1):
    a=65
    #for k in range(1,spaces+1):
        #print(' ',end=' ')
    for j in range(1,num+1):
        print(chr(a),end=' ')
        a+=1
    print()
    num+=1 
    #spaces-=1  
            


A 
B C
D E F
G H I J
K L M N O




n=5
num=1
a=65
#spaces=n-1
for i in range(1,n+1):
    
    #for k in range(1,spaces+1):
        #print(' ',end=' ')
    for j in range(1,num+1):
        print(chr(a),end=' ')
        a+=1
    print()
    num+=1 
    #spaces-=1


    A 
   A A
  A A A
 A A A A
A A A A A    




n=5
a=65
for i in range(1,n+1):
    print(' '*(n-i)+(chr(a)+' ')*i)

'''

# n=5
# spaces=2*n-1
# stars=1
# for i in range(1,2*n):
#     d=i
#     for j in range(1,spaces+1):
#         print(' ',end=' ')
#     for k in range(1,stars+1):
#         print(d,end=' ')
#         if k<=stars//2:
#             d-=1
#         else:
#            d+=1
          
#     print()

#     if i<2*n//2:
#         spaces-=1 
#         stars+=2  
#     else:
#         spaces+=1
#         stars-=2             

# n=5
# s=''
# for i in range(1,n+1):
#     s=str(i)+' '+s
#     print('  '*(n-i)+s)
# for j in range(n-1,0,-1):
#     print('  '*(n-j),end='')
#     for k in range(j,0,-1):
#         print(k,end=' ')
#     print()
        
        
'''
1
  2
    3
  4
5




n=5
for i in range(1,n+1):
    if i<=n//2+1:
        print('  '*(i-1)+str(i))
    else:
        print('  '*(n-i)+str(i))    
       
    


1
  2
    3
      4
    5
  6
7





n=7
for i in range(1,n+1):
    if i<=n//2+1:
        print('  '*(i-1)+str(i))
    else:
        print('  '*(n-i)+str(i))



1
  2
    3
  5
4



n=5
for i in range(1,n+1):
    if i<=n//2+1:
        print('  '*(i-1)+str(i))
    else:
        print('  '*(n-i)+str(2*n-i-1))





1
  2
    3
      4
    7
  6
5




n=7
for i in range(1,n+1):
    if i<=n//2+1:
        print('  '*(i-1)+str(i))
    else:
        print('  '*(n-i)+str(2*n-i-2))
   
    


1
  3
    5
  4
2



n=5
for i in range(1,n+1):
    if i%2!=0:
        print(' '*(i-1)+str(i)) 
for j in range(n,0,-1):
    if j%2==0:
        print(' '*(j-2)+str(j))
          
    




1
  3
    5
      7
    6
  4
2



n=7
for i in range(1,n+1):
    if i%2!=0:
        print(' '*(i-1)+str(i)) 
for j in range(n,0,-1):
    if j%2==0:
        print(' '*(j-2)+str(j))
          




2
  3
    5
      7
    11
  13
17


num=7
n=2
l=[]
c=0
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1  
        if c<=num:
            l+=[n]
        else:
            break
    n+=1        

for j in range(len(l)):
    if j<=len(l)//2:
        print('  '*(j)+str(l[j]))   
    else:
        print('  '*(len(l)-1-j)+str(l[j]))         


        


        


1
  3
    5
      7
        9
      8
    6
  4
2           



n=9
for i in range(1,n+1):
    if i%2!=0:
        print(' '*(i-1)+str(i)) 
for j in range(n,0,-1):
    if j%2==0:
        print(' '*(j-2)+str(j))



2
  3
    5
      8
    13
  21
34



n=7
a=0
b=1
l=[]
# print(a)
# print(b)
for i in range(2,n+3):
    
    c=a+b
    if c>1:

        l+=[c]
    a=b
    b=c  
    
for j in range(len(l)):
    if j<=len(l)//2:
        print('   '*j+str(l[j]))
    else:
        print('   '*(len(l)-1-j)+str(l[j]))      
    




* * * * * 
*       *
* * * * *
*       *
* * * * *


n=5
for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n//2+1:
        print(' '*(n//2-i)+'* '*n)
    elif i==n:
        print(' '*(n-i)+'* '*n)
    else:
        print('* '+'  '*(n-2)+'* ')            



* * * * * 
*
*
*
* * * * *




n=5

for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n:
        print(' '*(n-i)+'* '*n)
    else: 
        print('* ')    
    
  

* * * * * 
*       *
*       *
*       *
* * * * *




n=5
for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n:
        print(' '*(n-i)+'* '*n)
    else: 
        print('* '+'  '*(n-2)+'* ')       



* * * * * 
*
* * * * *
*
* * * * *



n=5
for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n//2+1:
        print('* '*n)    
    elif i==n:
        print(' '*(n-i)+'* '*n)
    else: 
        print('* '+'  '*(n-2)) 

  



* * * * * 
*
* * * * *
*
*

n=5
for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n//2+1:
        print('* '*n)    
    else: 
        print('* '+'  '*(n-2))
 

* * * * * * * * * * 
*
*
*
*
*       * * * * * * * *
*                 *   *
*                 *   *
*                 *   *
* * * * * * * * * *   *




n=10
for i in range(1,n+1):
    if i==1:
        print(' '*(i-1)+'* '*n)
    elif i==n//2+1:
        print('* '+'  '*(n-i-1)+'* '*(i+2)) 

    elif i==n:
        print('* '*(n)+'  '+'* ')

    elif i>=n//2+1:
       print('* '+'  '*(n-2)+'* '+'  '+'*')
    else:
        print('* ')   



*       * 
*       *
* * * * *
*       *
*       *


n=5
for i in range(1,n+1):
    if i==n//2+1:
        print('* '*n)    
    else:
        print('* '+'  '*(n-2)+'* ')    
    



* * * * * 
    *
    *
    *
* * * * *

n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('* '*n) 
    else:
        print('  '*(n//2)+'*')       
    


* * * * * 
    *
    *
    *
* * *



n=5
for i in range(1,n+1):
    if i==1 :
        print('* '*n) 
    elif i==n:
        print('* '*(n//2+1))    
    else:
        print('  '*(n//2)+'*')   


*   * 
*  *
* *
*  *
*   *



n=5
for i in range(1,n+1):
    if i<=n//2+1:
        print('* '+' '*(n-i-2)+'* ')
    else:
        print('* '+' '*(i-3)+'* ')    

      
      

* 
*
*
*
* * * * *




n=5
for i in range(1,n+1):
    if i==n:
        print('* '*n)
    else:
        print('* ')    



*          *
*  *    *  *
*     *    *
*          *
*          *


n=5
for i in range(1,n+1):
    if i==1:
        print('* '+'   '*(n-i-1)+'*')

    elif i>1 and i<n//2+1:
        print('*'+'  *  '*(n-i-1)+'*')  
    elif i==n//2+1:
        print('*'+'  '*(n-i)+' *'+'  '*(n-i)+'*')     
    else:
        print('* '+'   '*(n-2)+'* ')    
      


n=5
for i in range(1,n+1):
    if i==1:
        print('*'+' '*(n+1)+'*')
    else:
        print('*'+' '*(i)+'*') 
          


       1 
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
  1 5 10 10 5 1
 1 6 15 20 15 6 1






n=7
for i in range(1,n+1):
    num=1
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print(num,end=' ')
        num=num*(i-j)//j
    print()    


    
2
3 11
5 13 19
7 17 23 29
 
rows=4
n=2
c=0
l=[]
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        l+=[n]
        if c==rows*2+2:
            break             #0  1  2  3  4   5   6   7   8    9
    n+=1                     #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
a=0
b=3
for j in range(1,rows+1):
    for k in range(0,j):
        print(l[a],end=' ')
        if j<=rows//2:

            a+=3
        else:
            a+=b
            b-=1
    print()
    a=j
    b=3


7 8 9
6 1 2
5 4 3

 
rows=3
for i in range(1,rows+1):
    if i==1:
        print(rows)   
    print()    
    


* * * * *
  * * * *
    * * *
      * *
        *    

n=5
a=1
for i in range(1,n+1):
    if i<=n//2+1:
        print(')

'''  
'''
n=5
spaces=n
nums=1
for i in range(1,n+1):
    a=2
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(nums):
        print(a,end=' ')
        if k<nums//2:
            a+=2
        else:
            a-=2
    print()
    spaces-=1
    nums+=2            

'''