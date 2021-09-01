#################### PART 1 ####################
#Decrypt
f = open("private.key",'r')  
d = int(f.readline())
n = int(f.readline())

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
stdout_fileno.write(sample_input) #byte 

#################### PART 2 ####################
#readint input.txt.enc file as binary
f = open("input.txt.enc", 'r')
b_Cipher_txt = f.read()

#split input.txt into max_c_block_bit
num_chunk = int (len(b_Cipher_txt)/max_C_block_bit)
input_byte = [[0 for i in range(max_C_block_bit)] for j in range(num_chunk)] 

for j in range(0,num_chunk):
    input_byte[j] = b_Cipher_txt[(max_C_block_bit*j):(max_C_block_bit*j)+max_C_block_bit]

#Decimal into Binary
def DtoB(n):
    return bin(n).replace("0b","")

#Binary into Decimal
def BtoD(n):
    return int(n,2)

Plain_txt=[]
for j in range(0,num_chunk):
    Plain_txt.append(BtoD(input_byte[j]))

# C^d
for i in range(0,num_chunk):
    Plain_txt[i] = Plain_txt[i] ** d

# C^e mod n
for i in range(0,num_chunk):
    Plain_txt[i] = Plain_txt[i] % n

#Convert to Binary
for i in range(0,num_chunk):
    Plain_txt[i] = DtoB(Plain_txt[i])

#Byte into Character
Character=[]
for i in range(0,num_chunk):
    Character.append(chr(int(str(Plain_txt[i]),2)))

output_txt = ''.join(Character)

#writing the output_txt
f_out = open("output.txt", "w")
f_out.write(output_txt)


