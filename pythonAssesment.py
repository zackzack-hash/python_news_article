from collections import Counter
import string

def count_specific_word(text, target_word):
    if not text or not isinstance(text, str):
        return 0
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    
    # Structure requirement: Explicit for loop
    count = 0
    for w in words:
        if w == target_word.strip().lower():
            count += 1
    return count

def identify_most_common_word(text):
    if not text or not text.strip():
        return None
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    if not words:
        return None
        
    word_counts = Counter(words)
    res = word_counts.most_common(1)  # Example: [('banana', 3)]
    
    # CRITICAL FIX: Safe extraction using .pop() to avoid any bracket bugs
    if res:
        top_tuple = res.pop()       # Extracts ('banana', 3)
        word_string = top_tuple[0]  # Extracts 'banana'
        return word_string
    return None

def calculate_average_word_length(text):
    if not text or not text.strip():
        return 0.0
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_text.split()
    if not words:
        return 0.0
        
    # Structure requirement: Explicit for loop
    total_char_length = 0
    for word in words:
        total_char_length += len(word)
        
    return float(total_char_length / len(words))

def count_paragraphs(text):
    if not text or not text.strip():
        return 1
    raw_paragraphs = text.split("\n\n")
    
    # Structure requirement: Conditional statement
    paragraphs = []
    for p in raw_paragraphs:
        if p.strip():
            paragraphs.append(p)
            
    return len(paragraphs)

def count_sentences(text):
    if not text or not text.strip():
        return 1
        
    count = 0
    index = 0
    
    # Structure requirement: Explicit while loop tracking characters
    while index < len(text):
        if text[index] in ['.', '!', '?']:
            count += 1
            while index + 1 < len(text) and text[index + 1] in ['.', '!', '?']:
                index += 1
        index += 1
        
    if count == 0 and text.strip():
        return 1
        
    return count

if __name__ == "__main__":
    pass