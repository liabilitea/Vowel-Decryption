#Use dictionary to define the subtitutes

char_substitute = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}

#Prompt the user to input a text
encrypted_text = input("\033[3mEnter an encrypted text to decrypt:\033[0m ")

decrypted_text = ""

#Check if a character from the dictionary is present in the encrypted_text
#If character is present, it will retrieve the value and will be appended to decrypted text
for char in encrypted_text:
    if char in char_substitute:
        decrypted_text += char_substitute[char]
    else:
        decrypted_text += char

#Print the output