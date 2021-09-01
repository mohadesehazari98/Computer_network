#################### PART 1 ####################
#Get inputs {p,q}
p = int(input("please enter p, pay attention your number must be prime and p*q>256 , thank U :) : \n"))
q = int(input("please enter q, again your number must be prime and p!=q : \n"))

#check wether p & q are equal or not
if (p==q):
    print("p=q, you must enter two different prime number, sorry try again :(")
    exit()

#check whether the inputs are prime or not
#check p
if p > 1:
   for i in range(2,p):
       if (p % i) == 0:
           print("p must be a prime number, sorry try again")
           exit()
           break
#all numbers less than 1 are not prime so:
else:
   print("p must be a prime number, sorry try again")
   exit()

#check q
if q > 1:
   for i in range(2,q):
       if (q % i) == 0:
           print("q must be a prime number, sorry try again")
           exit()
           break
#all numbers less than 1 are not prime so:
else:
   print("q must be a prime number, sorry try again")
   exit()

#check wheter n=p*q > 256 or not
n=p*q
if (n<=256):
    print("For RSA algorithm we need p*q > 256 , your numbers didnt match the condition, try again for different p & q, O_O")
    exit()

#################### PART 2 ####################
import random
Phi_n = (p-1)*(q-1)
#generate e / conditioned 1) to be less than Phi(n) and 2)to be coprime with Phi(n)
#1)
random_list=[Phi_n-1]
#2)
def coprime2(a, b):
    P=0
    for i in range(2,a+1):
        if (a % i==0) and (b % i==0):
            P=1
            return False
    if P==0:
        return True

for i in range(2,Phi_n):
    if(coprime2(Phi_n - i,Phi_n)):
        random_list.append(Phi_n - i)
random_list.remove(1)        

e=random.choice(random_list)
#generate d using Euclidean algorithm
def find_d(Phi_n,e):
    Divisor = [Phi_n]
    Quotient = [e]
    Remainder = []
    Dividend = []
    level=0
    Done=1
    while Done:
        
        Dividend.append(Divisor[level] // Quotient[level])
        Remainder.append(Divisor[level] % Quotient[level])
        Divisor.append(Quotient[level])
        Quotient.append(Remainder[level])
        if Remainder[level]==1 :
            Done=0
            Divisor.remove(Divisor[level+1])
            Quotient.remove(Quotient[level+1])
        level=level+1

    state = []
    state.append(1)
    state.append(-Dividend[0])
    for i in range(2,len(Dividend)+1):
        state.append(state[i-2]-Dividend[i-1]*state[i-1])

    d = state[len(Dividend)]
    if d<0 :
        d=Phi_n + d
    return d
d = find_d(Phi_n,e)
print("P, Q, n, Phi(n), e & d in order")
print(p,q,n,Phi_n,e,d,sep=' /')
print("keygen.py *_*")
#################### PART 3 ####################
#private key
f_1 = open("private.key", "x")
f_1.write(str(d))
f_1.write("\n")
f_1.write(str(n))
f_1.close()

#public key
f_2 = open("public.key", "x")
f_2.write(str(e))
f_2.write("\n")
f_2.write(str(n))



