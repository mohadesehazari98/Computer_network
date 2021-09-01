#################### PART 1 ####################
#readint input.txt file as binary
f = open("input.txt", 'r')
plain_txt = f.read()
b_plain_txt = ''.join(format(ord(i), '08b') for i in plain_txt)

#split input.txt into bytes
num_chunk = int (len(b_plain_txt)/8)
input_byte = [[0 for i in range(8)] for j in range(num_chunk)] 
for j in range(0,num_chunk):
    input_byte[j] = b_plain_txt[(8*j):(8*j)+8]

#Encrypt
f = open("public.key",'r')  
e = int(f.readline())
n = int(f.readline())

#Decimal into Binary
def DtoB(n):
    return bin(n).replace("0b","")

#Binary into Decimal
def BtoD(n):
    return int(n,2)

Cipher_txt=[]
for j in range(0,num_chunk):
    Cipher_txt.append(BtoD(input_byte[j]))

# M^e
for i in range(0,num_chunk):
    Cipher_txt[i] = Cipher_txt[i] ** e

# M^e mod n
for i in range(0,num_chunk):
    Cipher_txt[i] = Cipher_txt[i] % n

#Convert to Binary
for i in range(0,num_chunk):
    Cipher_txt[i] = DtoB(Cipher_txt[i])

#Find maximum number of byte for C blocks
import math
max_C_block_byte = math.log(n, 256)
max_C_block_byte = math.ceil(max_C_block_byte)
max_C_block_bit = 8 * max_C_block_byte

#Stdout
import sys
stdout_fileno = sys.stdout
sample_input = max_C_block_byte
sample_input = str(sample_input)
stdout_fileno.write(sample_input)

#Resize blocks into 16bits
for i in range(0,num_chunk):
    Cipher_txt[i]=Cipher_txt[i].zfill(max_C_block_bit)

b_Cipher_txt = ''.join(Cipher_txt)

#writing the input.txt.enc
f = open("input.txt.enc", "x")
f.write(b_Cipher_txt)
f.close()
