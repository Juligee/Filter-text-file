# def shift(step):
#      alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                  'U', 'V', 'W', 'X', 'Y', 'Z']
#      shifted_alphabet = []
#      for i, item in enumerate(alphabet):
#          if i + step > len(alphabet):
#              left = (i + step) % len(alphabet)
#              item = alphabet[left]
#          elif i + step == len(alphabet):
#              item = alphabet[0]
#          else:
#              item = alphabet[i + step]
#          shifted_alphabet.append(item)
#      return alphabet, shifted_alphabet
 
 
# def encrypt(message):
#     alphabet, shifted_alphabet = shift(key)
#     index_array = []
#     encrypted = ''
#     for i in message.upper():
#         if i in alphabet:
#             ind = alphabet.index(i)
#             index_array.append(ind)
#         else:
#             index_array.append(i)

#     for n in index_array:
#         if type(n) is int:
#             encrypted += shifted_alphabet[n]
#         else:
#             encrypted += n

#             return encrypted
 
 
# def decrypt(message):
#     alphabet, shifted_alphabet = shift(key)
#     shifted_index = []
#     decrypted = ''
#     for i in message.upper():
#         if i in shifted_alphabet:
#             ind = shifted_alphabet.index(i)
#             shifted_index.append(ind)
#         else:
#             shifted_index.append(i)

#     for n in shifted_index:
#         if type(n) is int:
#             decrypted += alphabet[n]
#         else:
#             decrypted += n
#     return decrypted
 
 
# try:
#     operation = input("Do you want to (e)ncrypt or (d)ecrypt?: ").lower()
#     key = int(input("Please enter the key (0 to 26) to use.: "))
#     msg = input("Message: ")
#     if operation == "e":
#         print(encrypt(msg))
#     elif operation == "d":
#         print(decrypt(msg))
# except:
#     print("Please enter a valid operation")


#A python program to illustrate Caesar Cipher Technique

def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

def decrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + 65) % 26 - s + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + 97) % 26 - s + 97)

	return result

users_choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
text = input("Enter the message to encrypt or decrypt. DO NOT ADD(#,!.): ") # Don't add comma, full stop, etc to avoid plain text disconnection
s= int(input("Please enter the key (0 to 25) to use: "))

if users_choice == "e":
    x= encrypt(text,s)
    print(x)


else:
    if users_choice == "d":
        x= decrypt(text,s)
        print(x)

#check the above function

#s = 4
# print ("Text : " + text)
# print ("Shift : " + str(s))
# #print ("Cipher: " + encrypt(text,s))

# print ("Hello ! Welcome to JD's bank")
# print
# print ("Insert bank card and press any key to procede")
# print ()
# input()

# def mainMenu():

#     print ("------------------------------------------------")
#     print ("Select one of this options")
#     print ("1. Check Balance")
#     print ("2. Withdraw Money")
#     print ("3. Deposit Money ")
#     print ("0. Exit ")
#     print ("------------------------------------------------")

#     passcode = 1111

#     attempts = 0

#     #while passcode == 1111:

# passcodeInsertion= int(input("Please insert your 4-digit code: "))
      

# if passcodeInsertion == 1111:
#     print ("This is working") #testing-----
#     print ("")
#     print(mainMenu())



# # elif attempts < 2:

# #     print ("Sorry ! Wrong passcode")
# #     attempts += 1

# #     print ("------------------------------------------------")
# #     print ("")
# #     print("Try again !! This is your ") + str(attempts) + " attempt"
# #     print()
# #     print ("------------------------------------------------")
# #     print ()  

# else:
#     print("")
#     print ("Your card is unfortunately now blocked")
#     exit()