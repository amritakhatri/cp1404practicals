
"""
Word Occurrences
Estimate: 30 minutes
Actual: 60 minutes
"""

# Word Occurrences
user_input = input("Text: ")
words = user_input.split()

# Count occurrences of each word
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Find the maximum width for formatting
max_width = max(len(word) for word in word_counts.keys())

# Print word occurrences with aligned columns
for word, count in sorted(word_counts.items()):
    print(f"{word:>{max_width}} : {count}")

