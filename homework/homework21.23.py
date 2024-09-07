def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    return text.find(word)

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)

text_operations = {
    "word_count": word_count,
    "character_count": character_count,
    "find_word": find_word,
    "replace_word": replace_word
}

def process_text(text, operation, **kwargs):
    if operation in text_operations:
        if operation == "find_word":
            if "word" not in kwargs:
                raise ValueError("The 'find_word' operation requires a 'word' argument.")
            return text_operations[operation](text, kwargs["word"])
        elif operation == "replace_word":
            if "old_word" not in kwargs or "new_word" not in kwargs:
                raise ValueError("The 'replace_word' operation requires 'old_word' and 'new_word' arguments.")
            return text_operations[operation](text, kwargs["old_word"], kwargs["new_word"])
        else:
            return text_operations[operation](text)
    else:
        raise ValueError(f"Unsupported text operation: {operation}")

# Example usage
print(process_text("Hello world", "word_count"))
print(process_text("Hello world", "character_count"))
print(process_text("Hello world", "find_word", word="world"))
print(process_text("Hello world", "replace_word", old_word="world", new_word="Python"))

