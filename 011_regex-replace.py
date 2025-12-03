import re

text = "the quick brown fox jumps over the lazy brown dog"
pattern = r"brown"
replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("modified text: ", new_text)
