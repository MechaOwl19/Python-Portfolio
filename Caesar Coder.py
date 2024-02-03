alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 33
text = 'potat'
c_text = ''
                       
for char in text.lower():

    if char == ' ':
        c_text += char

    else:
        index = alphabet.find(char)
        index += shift % len(alphabet)
        
        c_text += alphabet[index]



print('text:',text)
print('ciphered text:', c_text)