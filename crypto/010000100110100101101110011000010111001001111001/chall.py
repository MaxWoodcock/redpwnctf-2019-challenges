from Crypto.PublicKey import *
from Crypto.Util.number import *

message = open("flag.txt","rb").read()
m = bytes_to_long(message)
n = 0
e = 65537
d = 0
ciphertext = 0

def setup():
	global n,d,ciphertext
	p = getPrime(512)
	q = getPrime(512)
	phiN = (p-1)*(q-1)
	d = inverse(e, phiN)
	n = p*q
	ciphertext = pow(m, e, n)

def decrypt(user_input):
	return str(pow(user_input, d, n) % 2)

setup()
print("011101010110110001110100011010010110110101100001011101000110010100100000011001010110111001100011011100100111100101110000011101000110100101101111011011100010000001110011011001010111001001110110011010010110001101100101\n")
print("0101011101000001010100100100111001001001010011100100011100111010001000000100100100100000011011110110111001101100011110010010000001110011011000010111100100100000001100000010000001101111011100100010000000110001\n")
print("0010100001001110001011000110010100101001: (" + str(bin(n)[2:]) + ", " + str(bin(e)[2:]) + ")\n")
print("0100010101001110010000110101001001011001010100000101010001000101010001000010000001001101010001010101001101010011010000010100011101000101: " + str(bin(ciphertext)[2:])+"\n")
while True:
	print("> ",end="")
	data = input()
	try:
		print(decrypt(int(data.strip(),2)))
	except Exception:
		print("Invalid input!")
		break
