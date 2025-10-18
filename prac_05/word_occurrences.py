"""
CP1404 Practical 5
Word Occurrences
Estimate: 20 minutes
Actual:
"""

text = input("Enter text: ")
words = text.lower().split()
word_count = {}

for word in words:
    word = word.strip(",.!?\;""'")
    word_count[word] = word_count.get(word, 0) + 1

print(f"Text: {text}")
for word, count in word_count.items():
    print(f"{word}: {word_count[word]}")




