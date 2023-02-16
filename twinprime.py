n1=int(input('choose one number'))
n2=int(input('choose a second number'))
c1=0
c2=0
for i in range(1,n1+1,1):
    if n1%i==0:
        c1=c1+1

for i in range(1,n2+1,1):
    if n2%i==0:
        c2=c2+1

if c1==2 and c2==2 and (n2-n1==2 or n1-n2==2):
    print(n1,n2,"are twin primes")

else:
   print(n1,n2,"are not twin primes")