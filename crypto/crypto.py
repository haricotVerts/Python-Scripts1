
#!/usr/bin/env python3 -tt
""" File: crypto.py """


""" This program has functions that encrypt and decrypt messages using 
    the caesar, Vigenere, and Merkle-Hellman ciphers.
"""

import random
import itertools
import utils
	


"""
Caesar Cipher
"""

def encrypt_caesar(plaintext, ROT_Val=3):
	"""
	Encrypts plaintext using a Caesar cipher.
	
	List comprehension works by creating a dictionary where the key value 
	is an alphabet letter and the key value is key letter shifed by ROT_Val.
	
	Then for each letter in the plantext input we lookup the cooriponsing 
	keyvalue from the dictionary and return the joined value.
	"""
    
    # If the plaintext is empty exit
	if not len(plaintext):
		return "Empty text value"
		
  
	alphabet      = "abcdefghijklmnopqrstuvwxyz" # Refrence alphabet
	plaintext     = plaintext.lower()		      # Simplify cipher by my forcing lowecase inputs
	
    # Dictionary key is the normal alphabet, the key-value is the coorisponding shifted letter
    # If there is a rot= 3. Dictionary => A: d, B:e, C:f, D:g,.... 
	encrypt_dict  = dict(zip(alphabet, alphabet[ROT_Val:] + alphabet[:ROT_Val]))
    
    # Each plaintext character is put into the dictionary as a key, and the shifted value is returned, and joined
    # Get has default set qual to the input inncase of unrecognized character
	text_encrypt  = ''.join([encrypt_dict.get(chr, chr) for chr in  plaintext])
	
	return text_encrypt

    

def decrypt_caesar(ciphertext, ROT_Val=3):
	"""
	Decrypts a ciphertext using a Caesar cipher.
	
	List comprehension works by creating a dictionary where the key value 
	is an alphabet letter shifted by ROT_Val and the key value is the cooriponsing
	alphabet letter.
	
	Then for each letter in the plantext input we lookup the cooriponsing 
	keyvalue from the dictionary and return the joined value.
	"""
    
    # If the plaintext is empty exit
	if not len(ciphertext):
		return "Empty text value"

	alphabet      = "abcdefghijklmnopqrstuvwxyz" # Refrence alphabet
	plaintext     = ciphertext.lower()		     # Simplify my forcing lowecase inputs
	
    # Dictionary key is the is the shifted alphabet value, the key-value is the normal alphabet value
    # If there is a rot= 3. Dictionary =>  d: a, e:b, f:c, g:d, .... 
	decrypt_dict  = dict(zip(alphabet[ROT_Val:] + alphabet[:ROT_Val], alphabet))
    
    # Ech character is put into the dictionary ane the converted value is returned and then joined
	text_decrypt  = ''.join( map( lambda chr: decrypt_dict.get(chr, chr), plaintext))
	
	return text_decrypt
	

	
	
"""
Vigenere Cipher
"""

def encrypt_vigenere(plaintext, keyword):
	"""
	Encrypts plaintext using a Vigenere cipher with a keyword.
    
    The keyword value is converted to a number and used to shift each plaintext character. 
    Then a for loop checks each character to see if it is out of the ASCII range, if so
        it is adjusted.
	"""
    # Put in lowertext form to simplify
	plaintext  = plaintext.lower()
	keyword    = keyword.lower()

	# Dictionary that attaches a value for each character
	shift_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 
				  'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18,
				  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25 }
	
    # zip the plaintext with each letter of the keyword. EX plaintext = abcd, kekword = zac => a,z  b,a  c,c  d,z
    # for each pair, sum ASCii of plaintext char, with keyvalue shift_dict value, then output turn ASCII value to char
	text_shift = ''.join( [chr(( (ord(x)+shift_dict[y])) ) for x, y  in zip(plaintext, itertools.cycle(keyword)) ] )
	
    
    # Ascii letter is 97 to 122, check if the value is in range and then shift.
	text_shift1 = []
    
	for x in text_shift:
        # modulo gets overflow value, and this is added to 96 for wrap value
		if ord(x) > 122:
			text_shift1.append(chr((ord(x)%122)+96))
            
		else:
			text_shift1.append(x)
			
 	return ''.join(text_shift1)

    

def decrypt_vigenere(ciphertext, keyword):
	"""
	Decrypts ciphertext using a Vigenere cipher with a keyword.
    
    The keyword value is converted to a number and used to shift each plaintext character. 
    Then a for loop checks each character to see if it is out of the ASCII range, if so
        it is adjusted.
	"""
    # Put in lowertext form to simpliify
	ciphertext = ciphertext.lower()
	keyword    = keyword.lower()
	
	# Dictionary that attaches a value for each character
	shift_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 
				  'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18,
				  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
	
    # zip the cyphertext with each letter of the keyword. EX cyphertext = abcd, kekword = zac => a,z  b,a  c,c  d,z
    # for each pair, subtract ASCII of cyphertext char, with keyvalue shift_dict value, then output turn ASCII value to char
	text_shift = ''.join( [chr(( (ord(x)-shift_dict[y])) ) for x, y  in zip(ciphertext, itertools.cycle(keyword)) ] )
	
    # Ascii letter is 97 to 122, check if the value is in range and then shift.
	text_shift1= []
    
	for x in text_shift:
        # mod value gives us the amount below the ASCII bounds, and then we subtract from 123 to get the in bound value
		if ord(x) < 97:
			text_shift1.append(chr(123-(97%ord(x))))
		else:
			text_shift1.append(x)
			
 	return ''.join(text_shift1)
	
	
	
    
	
"""
Merkle-Hellman Knapsack Cryptosystem
"""

def generate_private_key(n=8):
	"""Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem
	Following the instructions in the handout, construct the private key components
	of the MH Cryptosystem. This consistutes 3 tasks:
	1. Build a superincreasing sequence `w` of length n
		(Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
	2. Choose some integer `q` greater than the sum of all elements in `w`
	3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)
	You'll need to use the random module for this function, which has been imported already
	Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!
	@param n bitsize of message to send (default 8)
	@type n int
	@return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
	"""
	
	# Create a superincreasing sequence n bits long
	super_inc_seq = []
	super_inc_seq.append( random.randint(1, 10) )
		
	sum1 = super_inc_seq[0]
    
	for x in range(n-1):
		temp  = random.randint(sum1+1, 2*sum1)
 		sum1 += temp
		super_inc_seq.append(temp)
		
	# Random number greater than sum of superincreasing sequence
	q = random.randint(sum(super_inc_seq)+1, 2*sum(super_inc_seq))
		
	# Random coprime intiger
	r = random.randint(2, q-1)
	
	while not utils.coprime(q, r):
		r = random.randint(2, q-1)
		
	
	return tuple(super_inc_seq), q, r
	
	
    
def create_public_key(private_key):
	"""Creates a public key corresponding to the given private key.
	To accomplish this, you only need to build and return `beta` as described in the handout.
		beta = (b_1, b_2, ..., b_n) where b_i = r * w_i mod q
	Hint: this can be written in one line using a list comprehension
	@param private_key The private key
	@type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
	@return n-tuple public key
	"""
    
    # Unpack the private_key, then use fornula to create the public key
    # private_key is example ((3, 5, 14, 43, 92, 168, 643, 1506, 3277), 5984, 3151)
	w, q, r = private_key
	b = [r*x%q for x in w ]
	
	
	return tuple(b)
  

  
def encrypt_mh(message, public_key):
	"""Encrypt an outgoing message using a public key.
	1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
	2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
	3. Encrypt the 8 message bits by computing
		c = sum of a_i * b_i for i = 1 to n
	4. Return a list of the encrypted ciphertexts for each chunk in the message
	Hint: think about using `zip` at some point
	@param message The message to be encrypted
	@type message bytes
	@param public_key The public key of the desired recipient
	@type public_key n-tuple of ints
	@return list of ints representing encrypted bytes
	"""
    
	b_n =  public_key
	c  = []
	
    # each character is taken, converted into binary, and apply the encription to each bit. Then repacked.
	for char in message:
		a_n =  utils.byte_to_bits(ord(char))
	
		c.append( sum([x*y for x,y in zip(a_n, b_n)]) )
	
	return c

    
    
def decrypt_mh(message, private_key):
	"""Decrypt an incoming message using a private key
	1. Extract w, q, and r from the private key
	2. Compute s, the modular inverse of r mod q, using the
		Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
	3. For each byte-sized chunk, compute
		c' = cs (mod q)
	4. Solve the superincreasing subset sum using c' and w to recover the original byte
	5. Reconsitite the encrypted bytes to get the original message back
	@param message Encrypted message chunks
	@type message list of ints
	@param private_key The private key of the recipient
	@type private_key 3-tuple of w, q, and r
	@return bytearray or str of decrypted characters
    complex math, and the explanations are on https://github.com/stanfordpython/python-assignments/blob/master/assign1/README.md
	"""
    
	message_decrypt = []
	w, q, r         = private_key
	c               = message
	
	s               = utils.modinv(r, q)
	c_Prime         = []
	
	for char1, char2 in zip(message, w):
		#a_n =  utils.byte_to_bits(ord(char))
		#c.append( sum([x*y for x,y in zip(a_n, b_n)]) )
		
		c_Prime.append(char1*s%q)
	

    # Solve the superincreasing subset sum using c' and w to recover the original byte
	for letter in c_Prime:
		temp = letter
		zzz  = []
			
		for char in w[::-1]:
			if temp  >= char:
				temp -= char
				zzz.append(1)
			else:
				zzz.append(0)
			
		message_decrypt.append( chr(utils.bits_to_byte(zzz[::-1])) )

	
	return ''.join(message_decrypt)




if __name__ == '__main__':
    ##### c
    print decrypt_caesar(encrypt_caesar("zac HER!"))
    print decrypt_caesar(encrypt_caesar("Python @"))
    
    print "######"
    
    
    ##### v
    print decrypt_vigenere(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LEMON") # "ATTACKATDAWN"
    print decrypt_vigenere(encrypt_vigenere("ATTACKATDAWN", "Lemon"), "Lemon") # "ATTACKATDAWN"
    
    print "######"
  
 
	##### M
    a = generate_private_key()
    b = create_public_key(a)
    c = encrypt_mh("ZAch!alp", b)
    print decrypt_mh(c, a)
	
    
    
	


