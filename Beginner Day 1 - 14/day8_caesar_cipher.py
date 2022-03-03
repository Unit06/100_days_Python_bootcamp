# Caesar Cipher day 8 project
import day7_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
temp_text = []

print(day7_art.logo2)
direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(raw_text, user_shift):
    for i in raw_text:
        if (alphabet.index(i)+user_shift+1) > len(alphabet):
            temp_text.append(alphabet[(alphabet.index(i) + user_shift) % (len(alphabet))])
        else:
            temp_text.append(alphabet[alphabet.index(i) + user_shift])
    print("The encoded text is ", ''.join(temp_text))


def decrypt(raw_text, user_shift):
    for i in raw_text:
        if (alphabet.index(i)-user_shift) < 0:
            temp_text.append(alphabet[(alphabet.index(i) - user_shift) % (len(alphabet))])
        else:
            temp_text.append(alphabet[alphabet.index(i) - user_shift])
    print("The decoded text is ", ''.join(temp_text))


if direction == "1":
    encrypt(text, shift)
if direction == "2":
    decrypt(text, shift)