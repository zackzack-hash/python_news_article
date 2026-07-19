import re
from collections import Counter
from docx import Document

def get_words(text):
    return re.findall(r"\b\w+\b", text.lower())


# Read the document
def read_document(file_path):

    docx = Document(file_path)
    paragraphs = []

    for paragraph in docx.paragraphs:
        paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


# Count specific word
def count_specific_word(text, search_word):
    words = get_words(text)
    search_word = search_word.lower()
    count = 0
    index = 0
    while index < len(words):
        if words[index] == search_word:
            count += 1
        index += 1
    return count
# Identify most common word
def identify_most_common_word(text):
    words = get_words(text)

    if not words:
        return None
    else:
        return Counter(words).most_common(1)[0][0]


# Calculate average word length
def calculate_average_word_length(text):
    words = get_words(text)

    if not words:
        return 0
    else:
        total = 0
        for word in words:
            total += len(word)
        return total / len(words)


# Count paragraphs
def count_paragraphs(text):
    if not text.strip():
        return 1
    else:
        paragraphs = re.split(r"\n\s*\n", text.strip())
        return len(paragraphs)
# Count sentences
def count_sentences(text):
    if not text.strip():
        return 1
    else:
        sentences = re.findall(r"[^.!?]+[.!?]", text)
        return len(sentences)


# ---------------- MAIN PROGRAM ----------------


if __name__ == "__main__":
    # Path to news article document
    file_path = "News Article for Python Assessment.docx"

    # Read the document
    text = read_document(file_path)

    # Ask the user for a search word
    word = input("Enter the word to search: ")

    # Display results
    print("Occurrences:", count_specific_word(text, word))
    print("Most common word:", identify_most_common_word(text))
    print("Average word length:", calculate_average_word_length(text))
    print("Paragraphs:", count_paragraphs(text))
    print("Sentences:", count_sentences(text))