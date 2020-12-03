# MADE BY JAY

def encrypt(msg, key):
    cipher = ''
    for char in msg:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)

    return cipher


def decrypt(msg, key):
    cipher = ''
    for char in msg:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - key - 97) % 26 + 97)

    return cipher

choice = int(input("Enter Choice: \n 1 = encryption , 2 decryption : "))
# key = int(input("Enter KEY: "))

if choice == 1:

    message = input("Enter MESSAGE: ")
    print("Original Message: ", message)

    for key in range(0,26) :
        print("Key : ",key ,"encryption: ", encrypt(message,key))

elif choice == 2:
    message = input("Enter MESSAGE: ")
    print("Message To Decrypt : ", message)
    for dkey in range(0, 26):
        print("Key : ",dkey ,"Decryption: ", decrypt(message, dkey))
else:
    print(" Try Again -> ")