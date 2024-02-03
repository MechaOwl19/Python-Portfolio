text = 'Hello Zaira!'
custom_key = 'python'

def vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():  
         #.isalpha gives true if everything in the string is letters
         # not reverts true to false
            encrypted_text += char
        else:
            #find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            #define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
            return encrypted_text
        
encryption = vigenere (text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key)
print(decryption)
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)
