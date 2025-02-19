
import re
from collections import Counter
def most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    most_common = Counter(words).most_common(1)[0][0]
    return most_common
text = input("Enter a paragraph: ")
print("The most common word is:", most_common_word(text))

