"""
CP1404 Practical 5
Word Occurrences
Estimate: 20 minutes
Actual: 28 minutes
"""

text = input("Enter text: ")
words = text.lower().split()
word_count = {}

for word in words:
    word = word.strip(",.!?\;""'")
    word_count[word] = word_count.get(word, 0) + 1

print(f"Text: {text}")

sorted_words = list(word_count.keys())
sorted_words.sort()

word_length = max(len(word) for word in sorted_words)

for word, count in word_count.items():
    print(f"{word:{word_length}} : {word_count[word]}")




