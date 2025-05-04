alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift):
    encrypted_text = ""
    for letter in original_text:
        #print(letter)
        shift_amount = shift
        if not letter.isalpha():
            encrypted_text += letter

        else:
            # i is the index of the current letter in the original text in the alphabet
            i = alphabet.index(letter)
            #print(i)
            while i + shift_amount >= len(alphabet):
                shift_amount -= len(alphabet)
            encrypted_text += alphabet[i + shift_amount]

    print(encrypted_text)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)




# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

