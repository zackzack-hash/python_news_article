from collections import Counter
import re
import string

def count_specific_word(text, target_word):
    """Counts the occurrences of a specified word in the text.
    Edge Case: If no matches are found or text is empty, returns 0.
    """
    if not text or not isinstance(text, str):
        return 0
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    return words.count(target_word.strip().lower())

def identify_most_common_word(text):
    """Identifies the most common word in the text.
    Edge Case: An empty string returns None.
    """
    if not text or not text.strip():
        return None
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    if not words:
        return None
    word_counts = Counter(words)
    res = word_counts.most_common(1)
    return res[0][0] if res else None

def calculate_average_word_length(text):
    """Calculates the average length of words in the text, excluding punctuation.
    Edge Case: An empty string returns 0.0.
    """
    if not text or not text.strip():
        return 0.0
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_text.split()
    if not words:
        return 0.0
    total_char_length = sum(len(word) for word in words)
    return float(total_char_length / len(words))

def count_paragraphs(text):
    """Counts paragraphs based on empty lines between blocks of text.
    Edge Case: An empty string returns 1.
    """
    if not text or not text.strip():
        return 1
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)

def count_sentences(text):
    """Counts sentences based on punctuation marks (., !, ?).
    Edge Case: An empty string returns 1.
    """
    if not text or not text.strip():
        return 1
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    return len(sentences)

if __name__ == "__main__":
    # Sample Test Inputs for manual verification
    sample_text = "This is a test. This is only a test!\n\nHere is a second paragraph with some apples."
    
    print("--- Local Tests Execution ---")
    print(f"1. Target Word 'test' Count: {count_specific_word(sample_text, 'test')}")
    print(f"2. Most Common Word String:  '{identify_most_common_word(sample_text)}'")
    print(f"3. Avg Word Length (Float):   {calculate_average_word_length(sample_text):.2f}")
    print(f"4. Paragraph Count (Int):    {count_paragraphs(sample_text)}")
    print(f"5. Sentence Count (Int):     {count_sentences(sample_text)}")
    print("-" * 30)