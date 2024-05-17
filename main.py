def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_letters(text)
    report = print_report(char_dict)
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

def print_report(chars):
    sorted_dict = dict(sorted(chars.items()))
    for char in sorted_dict: 
        if char.isalpha() == True:
            print(f"The '{char}' character was found {sorted_dict[char]} times")
    
main()
