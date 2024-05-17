def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_letters(text)
    report = print_report(char_dict, num_words)
    print(report)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letters(text):
    answer = {}
    for char in text:
        lowered = char.lower()
        if lowered in answer: 
            answer[lowered] += 1
        else: 
            answer[lowered] = 1
            
    return answer

def print_report(chars, words):
    sorted_dict = dict(sorted(chars.items()))
    print("--- Report of character occurences in books/frankenstein.txt ---")
    print(f"There were {words} words found in the document.")
    print(" ")
    for char in sorted_dict: 
        if char.isalpha() == True:
            print(f"The '{char}' character was found {sorted_dict[char]} times")
            
    print("--- End of report ---")
    
main()
