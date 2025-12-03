import re

text = "the quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)

if search:
    print("word exists", search.group())
else:
    print("word doesn't exist")