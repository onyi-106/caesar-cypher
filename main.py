alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Insert a text/word:\n")
shift = int(input("How many shift:\n"))
alphabet_length = len(alphabet)
text_length = len(text)

def caesar(start_text=text, shift_amount=shift):
  end_of_command = False
  encrypted_text = ""
  if shift_amount >= 26:
    shift_amount = shift_amount % 26

  for letter in start_text:
      
    letter_position = alphabet.index(letter)
    new_position = letter_position + shift_amount
    encrypted_text += alphabet[new_position]
  
  print(encrypted_text)
caesar(start_text=text, shift_amount=shift)