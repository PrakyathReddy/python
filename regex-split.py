import re

text = "apple,banana,orange,grape"
pattern = r","

split = re.split(pattern, text)
print("split result would be: ",split)