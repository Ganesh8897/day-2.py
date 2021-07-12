alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt, type 'decode' to 'decrypt':\n")
text=inpute("type your message:\n")
shift=int(input("type the shift number:\n")

def encrypt(plane_text, shift_amount):
       cipher_text=""
       for letter in plane_text:
              position = alpha.indev(letter)
              new_position=posiition + shift_amount
               cipher_text +=alpha[new+position]
       print(f"the encodeed text is {cipher_text}") 
          
         
           
          
          
        
          
