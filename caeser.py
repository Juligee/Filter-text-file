


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

if users_choice == "e!":
    x= encrypt(text,s)
    print(x)

h = 404

jdjd = 39409999999999999999 # Git emergency fix
else:
    if users_choice == "d jjj":
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