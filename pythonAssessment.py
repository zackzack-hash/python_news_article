import re
from collections import Counter
from docx import Document


def get_words(text):
    """Helper function to extract clean words from text."""
    return re.findall(r"\b\w+\b", text.lower())


def read_document(file_path):
    """Reads paragraphs from a docx file using a for loop."""
    doc = Document(file_path)
    paragraphs = []
    for paragraph in doc.paragraphs:
        paragraphs.append(paragraph.text)
    return "\n".join(paragraphs)


def count_specific_word(text, search_word):
    """Counts occurrences of a specific word using a while loop and conditional."""
    words = get_words(text)
    search_word = search_word.lower()
    count = 0
    index = 0

    while index < len(words):
        if words[index] == search_word:
            count += 1
        index += 1

    return count


def identify_most_common_word(text):
    """Identifies the most common word, returning None if empty."""
    words = get_words(text)
    if not words:
        return None
    counts = Counter(words)
    return counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """Calculates average word length, returning 0 if text is empty."""
    words = get_words(text)
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def count_paragraphs(text):
    """Counts paragraphs separated by newlines."""
    if not text.strip():
        return 1
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len(paragraphs)


def count_sentences(text):
    """Counts sentences using regex pattern."""
    if not text.strip():
        return 1
    sentences = re.findall(r"[^.!?]+[.!?]", text)
    if not sentences:
        return 1
    return len(sentences)


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    file_path = "Assessment.docx"
    try:
        text = read_document(file_path)
        word = input("Enter the word to search: ")

        print("Occurrences:", count_specific_word(text, word))
        print("Most common word:", identify_most_common_word(text))
        print("Average word length:", calculate_average_word_length(text))
        print("Paragraphs:", count_paragraphs(text))
        print("Sentences:", count_sentences(text))
    except Exception as e:
        print(f"Error reading file: {e}")
