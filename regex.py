import re
regex_sentence = "I love to eat pizza and pasta 3 times a day"
# print(re.findall(r"a.d", regex_sentence))
# print(re.findall(r"pi.*ta", regex_sentence))
# print(re.findall(r"lo.+at", regex_sentence))
# print(re.findall(r"piz?za", regex_sentence))
# output
# ['and', 'a d']
# ['pizza and pasta']
# ['love to eat']
# ['pizza']

# print(re.findall(r"[aeiou]", regex_sentence))
# print(re.findall(r"[a-z]", regex_sentence))
# output
# ['o', 'e', 'o', 'e', 'a', 'i', 'a', 'a', 'a', 'a', 'i', 'e', 'a', 'a']
# ['l', 'o', 'v', 'e', 't', 'o', 'e', 'a', 't', 'p', 'i', 'z', 'z', 'a', 'a', 'n', 'd', 'p', 'a', 's', 't', 'a', 't', 'i', 'm', 'e', 's', 'a', 'd', 'a', 'y']

# print(re.findall(r"\d", regex_sentence))
# print(re.findall(r"\w", regex_sentence))
# print(re.findall(r"pizza\sand\spasta", regex_sentence))
# print(re.findall(r"\D", regex_sentence))
# print(re.findall(r"\W", regex_sentence))
# print(re.findall(r"\S", regex_sentence))
# ouput
# ['3']
# ['I', 'l', 'o', 'v', 'e', 't', 'o', 'e', 'a', 't', 'p', 'i', 'z', 'z', 'a', 'a', 'n', 'd', 'p', 'a', 's', 't', 'a', '3', 't', 'i', 'm', 'e', 's', 'a', 'd', 'a', 'y']
# ['pizza and pasta']
# ['I', ' ', 'l', 'o', 'v', 'e', ' ', 't', 'o', ' ', 'e', 'a', 't', ' ', 'p', 'i', 'z', 'z', 'a', ' ', 'a', 'n', 'd', ' ', 'p', 'a', 's', 't', 'a', ' ', ' ', 't', 'i', 'm', 'e', 's', ' ', 'a', ' ', 'd', 'a', 'y']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# ['I', 'l', 'o', 'v', 'e', 't', 'o', 'e', 'a', 't', 'p', 'i', 'z', 'z', 'a', 'a', 'n', 'd', 'p', 'a', 's', 't', 'a', '3', 't', 'i', 'm', 'e', 's', 'a', 'd', 'a', 'y']

text= "The quick brown fox jumps over the lazy dog 123 times"
x = re.search("\w+(?= times)", text)
print(x.group())  # Output: 123
