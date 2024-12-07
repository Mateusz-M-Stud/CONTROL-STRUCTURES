###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():
        # read the character's code (use ord())
        lc = ord(char)
        
        # add one to the character's code

        encrypted_text += chr(lc + 1)
    else:
         # add encrypted character to encrypted text
        encrypted_text += char

# Print original and encrypted text
print(plain_text)
print(encrypted_text)


#        if char == 'z':
#            encrypted_text += 'a'
#       elif char == 'Z':
#           encrypted_text += 'A'