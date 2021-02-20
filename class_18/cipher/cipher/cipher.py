
# Review Lab Submission
def encrypt(plain_text, key):
    """
    plain_text is a string or intigers
    key = an integer shift
    plain 12345 -> encrypted 23456
    """
    
    encrypted_pin = ''
    print(f'The plain text data is {plain_text}.')
    for char in plain_text:
        num = int(char) # 0 - 9
        # make a shifted num that is properly shifted bust still in range
        shifted_num = num + key

        # Use this to handle cases of numbers > 10 replace the if below
        shifted_num = (num + key) % 10
        #
        if shifted_num > 9:
            shifted_num -= 10
        encrypted_pin += str(shifted_num)
    print(f'The encrypted data with a shift of {key} is {encrypted_pin}.')
    print('#'*50)
    return encrypted_pin


def decrypt(encoded, key):
    return encrypt(encoded, -key)


if __name__ == "__main__":
    assert encrypt('12345', 1) == '23456'
    assert encrypt('12345', 2) == '34567'
    assert encrypt('12345', 3) == '45678'
    assert encrypt('12345', 9) == '01234'
    assert encrypt('12345', 21) == '23456'
    assert encrypt('12345', -1) == '01234'
    assert encrypt('23456', -1) == '12345'
    
    # There seems to be a coorelation between a shift of 1 and -1, can you spot it
    # Pause for student interaction
    # Lets test it with 5

    key = 5
    plain = '12345'

    encrypted = encrypt(plain, key)
    decrypted = encrypt(encrypted, -key)
    assert decrypted == plain

    # This feels a little clunky and not very programmitic.  Lets fix that..
    #  add Decrypt function
    
    print('All Done')


# So lets talk about where you will need to go from here.
# In your lab, you will not be working with numbers but alpha characters
# The idea of the code above will hold true.
# You may need to adjust your modulo a little and how you wrap around.


# Another part of your lab is to decrypt without the key.  So if I had the following:

# max
# qeb (4)
# lzw (-1)
# rfc (5)
# the (7)

# If you had to make an educated guess which of these was un-encrypted which would you pick?  Why?
# It is part of the english language.  It's not perfect, as it could equate to something else that is in the english language 

# the max comparison
