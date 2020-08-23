import re
s = "The quick brown fox jumps over the lazy dog"
vowel_list = set(re.findall("[a|e|i|o|u]",s))
#print(vowel_list)

if len(vowel_list)==5:
    print(f"All vowels are present in |{s}|")
else:
    print(f"Not all vowels are present in string |{s}|.Only {vowel_list} vowels found")



# single_quote ="'"
# fmt=r'\u'
# string = single_quote+fmt+'0933'+single_quote
# print(string)
# print('\u0933')

##reverse a number
print(re.sub(r'(\d+)*(\d+)',
       r'\2\1',
       '1234332'))

def f(match_obj):
    print(match_obj)
    m = match_obj.group(0)
    if m.isdigit():
        return str(int(m) * 10)
    else:
        return m.upper()


print(re.subn(r'\w+', f, 'foo.10.bar.20.baz.30'))

print(re.subn(r'\w+',f,'foo.10.bar.20.baz.30'))