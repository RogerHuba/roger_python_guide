import re
from nltk.corpus import words

words_list = words.words()


def encrypt(string, shift):
    cipher = ''

    for char in string:
        new_char = char
        if new_char.isalpha():
            offset = 97 if char.islower() else 65

            new_char = chr((ord(char) + shift - offset) % 26 + offset)

        cipher += new_char
    return cipher


def decrypt(string, shift):
    return encrypt(string, -shift)


def decrypt_blind(string):
    if not string:
        return None

    most_likely = ''
    max_pct = 0

    for shift in range(0,26):
        decrypted = decrypt(string, shift)

        decrypted_words = decrypted.split()

        english_count = 0

        for word in decrypted_words:
            cleaned_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
            if cleaned_word in words_list:
                english_count += 1

        percent_english = int(english_count / len(decrypted_words) * 100)

        if percent_english > max_pct:
            max_pct = percent_english
            most_likely = decrypted

    return most_likely


if __name__ == '__main__':
    encrypted_string = encrypt('The quick brown fox jumped over the lazily sleeping dog', 5)
    print(encrypted_string)
    most_like = decrypt_blind(encrypted_string)
    print(most_like)

