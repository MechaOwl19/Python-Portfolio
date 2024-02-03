

def bin_ciph(word):
    
    for char in word.lower():
        bin_txt = ''
        
        if char == 'a':
            bin_char = '01000001'
            bin_txt += bin_char

        elif char == 'b':
            bin_char = '01000010' 
            bin_txt += bin_char

        elif char == 'c':
            bin_char = '01000011'
            bin_txt += bin_char
            
        elif char == 'd':
            bin_char = '01000100' 
            bin_txt += bin_char

        elif char == 'e':
            bin_char = '01000101'
            bin_txt += bin_char
            
        elif char == 'f':
            bin_char = '01000110' 
            bin_txt += bin_char

        elif char == 'g':
            bin_char = '01000111'
            bin_txt += bin_char
            
        elif char == 'h':
            bin_char = '01001000' 
            bin_txt += bin_char

        elif char == 'i':
            bin_char = '01001001'
            bin_txt += bin_char
            
        elif char == 'j':
            bin_char = '01001010' 
            bin_txt += bin_char

        elif char == 'k':
            bin_char = '01001011'
            bin_txt += bin_char
            
        elif char == 'l':
            bin_char = '01001100' 
            bin_txt += bin_char

        elif char == 'm':
            bin_char = '01001101'
            bin_txt += bin_char
            
        elif char == 'n':
            bin_char = '01001110' 
            bin_txt += bin_char

        elif char == 'o':
            bin_char = '01001111'
            bin_txt += bin_char
            
        elif char == 'p':
            bin_char = '01010000' 
            bin_txt += bin_char

        elif char == 'q':
            bin_char = '01010001'
            bin_txt += bin_char
            
        elif char == 'r':
            bin_char = '01010010' 
            bin_txt += bin_char

        elif char == 's':
            bin_char = '01010011'
            bin_txt += bin_char
            
        elif char == 't':
            bin_char = '01010100' 
            bin_txt += bin_char

        elif char == 'u':
            bin_char = '01010101'
            bin_txt += bin_char
            
        elif char == 'v':
            bin_char = '01010110' 
            bin_txt += bin_char

        elif char == 'w':
            bin_char = '01010111'
            bin_txt += bin_char
            
        elif char == 'x':
            bin_char = '01011000' 
            bin_txt += bin_char

        elif char == 'y':
            bin_char = '01011001'
            bin_txt += bin_char
            
        elif char == 'z':
            bin_char = '01011010' 
            bin_txt += bin_char

        elif char == ' ':
            bin_txt += ' '

        print (bin_txt)

bin_ciph ('banana')