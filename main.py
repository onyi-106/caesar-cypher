alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Insert a text/word:\n")
shift = int(input("How many shift:\n"))
alphabet_length = len(alphabet)
text_length = len(text)


##MAKE THE LETTER IN THE TEXT SEPERATED AND STORED INSIDE A LIST##
def encrypt(text, shift):
  text_seperated = []

  for num in range(0, text_length):
    position = alphabet.index(text[num])
    # print(letter_from_text - 26)
    negative_position = position - alphabet_length
    # print(negative_position)
    negative_position_letter = alphabet[negative_position]
    
  
    ##AFTER SHIFTED##
    position_shifted = negative_position + shift
    letter_shifted = alphabet[position_shifted] 
  
    text_seperated += letter_shifted
    
    # print(negative_position_letter)
    # text_seperated.append(letter_from_text)
  text_encrypted = "".join(text_seperated)
  
  print(text_encrypted)
  # print(alphabet.index(text_seperated))
  
  # for num in range(0, len(text_seperated)):


encrypt(text=text, shift=shift)


#####################ALTERNATIVELY#####################

def encrypt(plain_text, shift_amount):

  cipher_text = ""
  #Immediately concatinate the element from the for() function below to the cipher_text without putting it inside a list first.
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)