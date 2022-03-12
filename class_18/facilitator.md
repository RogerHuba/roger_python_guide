# Demos: Cryptography

Use this document to describe the demo(s). Generally, this is going to take the format of either how to build the demo step by step, or less specifically, talking points surrounding the outcomes of the demo segment and code snippets to highlight.

## Demo 1 Number Cipher

> `../demo/crypto/number_cipher.py`

**QUESTION:** What is the Caesar Cipher.

**ANSWER:** One of the earliest and simples/gu t forms of encryption. It uses a shift value to shift the original text by that value.

Here is an example:

`IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`

Any guesses what that string is in unencrpyted form?

`The quick brown fox jumped over the lazy sleeping dog`

With a shift of 11 we get...
`IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`

That's what you'll be taking on in lab.

Lets see if we can generate a function to do something similar to this now.

Instead of letters, let's to use numbers.

We will start off by defining an encrypt method that takes in a plain text and a key.

```python
def encrypt(plain: str, key: int) -> str:
# plain text will be the unencrypted value
# The key will be the shift number
# plain: 12345
# key: 2
# -> 345678
```

First thing we do is give ourself an variable to store our return value.

```python
encrypted_text = ''
```

We now need to shift each number in our plain by the key.

A quick way to get through this is to iterate over the plain text.

```python
for num in plain:
    print(f"plain {num} not yet shifted by {key}")
```

A quick test shows that we can easily print out a few things.

```python
if __name__ == "__main__":
    encrypt('12345', 1)
    encrypt('345', 2)
```

> We tested that out, and we are hitting our function and iterating through the plain. Next lets shift our plain by the key.

```python
encrypted_number += num
```

Seems simple enough. But let's guess what is going to happen here?

We are trying to add a string and an int.  Error!

Need some type conversion here but we have to think through this one.

To GROUP: Looking for some ideas to fix this.  Will probably end up with this:

```python
for char in plain:
    num = int(char)
    shifted_number = num + key
    if shifted_number > 9:
        shifted_number -= 10
    encrypted_text += str(shitfed_number)
```

If students did not already arrive a solution  using mod then refactor to...

```python
shifted_num = (num + key) % 10
```

Final run through in main:

- key = 5
- plain = 12345
- encrypted = encrypt(plain, key)
- print(encrypted)
- decrypted = decrypt(encrypted, key)
- print(decrypted)
- assert decrypted = plain

Things seem to be working well for numbers.

How about for letters?

We want to do something like this...

- For the string `max`
  - shift max by 3 -> pda
  - shift max by 5 -> rfc
  - shift max by 7 -> the
- be able to get back `max` by decrypting it's encrypted form

## Demo 2 : Is English Word

> `../demo/crypto/is_english_word.py`

In order to automate the process of cracking Caesar Cipher then our programs must be able to have a sense of when an unencrypted string is likely to be correct. In other words, a candidate string that has many recognized words in it more likely to be correctly decrypted vs. a string that does not.

And in order for program to identify `known` words, it needs to actually know about them. That's what a corpus is for. And we can easily get access to a good one from `nltk`

Walk through the small amount of code in demo showing the import of corpus, the counting of known words in a phrase, and the basic report on percentage of known words in a phrase.

```python
import nltk
from nltk.corpus import words, names
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()

test_sentence = "hello from skjfhsdf"
word_list_test = test_sentence.split(' ')
for word in word_list_test:
    if word in word_list:
        print(f'{word} is here')
    else:
        print(f'{word} is not here')
```

[StackOverflow link](https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed)

[NLTK](https://www.nltk.org/data.html)
