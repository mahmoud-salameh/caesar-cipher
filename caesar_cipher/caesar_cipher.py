import nltk
from nltk.sem.logic import TRUTH_TYPE

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words,names

words_lest=words.words()
name_list=names.words()

def encrypt(text,rep):
    eresult=''
    text=text.lower()
    for p in (len(text)):
        cha = text[p]
        if (cha.isupper()):
         eresult += chr((ord(cha) + rep -65) % 26 + 65)
        else:
         eresult += chr((ord(char) + s - 97) % 26 + 97)
        return eresult
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                        translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
       
    return encrypted_eresult

def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


if __name__=='__main__':
    encrypt = encrypt(text, rep)
    decrypt = decrypt(encrypted_message, Kinv)

    print("Original message: " + text)
    print("Encrypted message: " + encrypt)
    print("Decrypted message: " + decrypt)