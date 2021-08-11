# Lecture NOTES: Intro to Crypto

## Review Today's Lab

### Encryption with Caesar Cipher

First let's review the Caesar Cipher

**QUESTION:** What is the Caesar Cipher.

**ANSWER:** One of the earliest and simplest forms of encryption. It uses a shift value to shift the original text by that value.

Here is an example:

`IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`

Any guesses what that string is in unencrpyted form?

`The quick brown fox jumped over the lazy sleeping dog`

With a shift of 11 we get...
`IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`

That's what you'll be taking on in lab.

Lets see if we can generate a function to do something similar to this now.

Instead of letters, let's to use numbers.

> Start Demo 1

Things seem to be working well for numbers.

How about for letters?

We want to do something like this...

- For the string `max`
  - shift max by 3 -> pda
  - shift max by 5 -> rfc
  - shift max by 7 -> the
- be able to get back `max` by decrypting it's encrypted form

That's pretty close to what we went over with numbers but there are a couple of key differences that will require some research. Because letters are not numbers, though they can be represented numerically. And they aren't limited to 10 choices.

> Don't mention to students yet but [ord](https://www.w3schools.com/python/ref_func_ord.asp) is the built in function they'll need.

### Cracking the Encryption

The lab requires us to not only encrypt an decrypt with a key, but also **WITHOUT** a key.

How the heck are we going to do that?

> Start Demo 2
