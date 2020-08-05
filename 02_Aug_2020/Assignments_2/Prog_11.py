'''11) WAP to get the count of words in the statement string and
the count of vowels in complete statement.'''

input_str = input("Enter the string")

## method to count the words
def count_words_in_str(f_str):
    fmt_sep = chr(32) ## chr(32) is for space
    cntr = 0
    word_count = 1
    str_len = len(f_str)
    if(str_len == 0):
        return 0

    for char in f_str:
        if char == fmt_sep or (cntr +1) == str_len:
            #print("word_count",word_count)
            word_count = word_count+1
        cntr = cntr + 1
    return word_count

##method to count the vowels
def count_vowels_in_str(f_str):
    cntr = 0
    vowels_list = ['a','e','i','o','u']
    vowel_count = 0
    consonant_count= 0
    while cntr < len(f_str):
        if f_str[cntr] in vowels_list:
            vowel_count += 1
        else:
            consonant_count += 1
        cntr += 1
    #print("vowel_count ",vowel_count)
    return vowel_count,consonant_count

Num_of_Words = count_words_in_str(input_str)
vowel_count,consonant_count = count_vowels_in_str(input_str)

print(f"number of words in string '{input_str}' is {Num_of_Words}")
print(f"number of vowels {vowel_count} and consonants {consonant_count}")