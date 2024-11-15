'''
Python code to check if a word is palindrome.
'''

# Ask for a word to check
word = input(print('Type the word you would like to check if it is palindrome: '))

# Declare some variables that are going to be needed below
len_wrd = len(word)
palindrome = True

# Check if the word is even or odd in length and make it even
if len_wrd % 2 != 0:
    new_len = (len_wrd - 1) / 2
elif len_wrd % 2 == 0:
    new_len = len_wrd / 2
new_len = int(new_len)

# Iterate through the word and compare each character in reverse order
for i in range(new_len):
    # If a character is not the same as the one being compared, then
    # the word is not a palindrome
    if word[i] != word[-i - 1]:
        palindrome = False

# Print the result
print('Is word', word, 'palindrome?:', palindrome)