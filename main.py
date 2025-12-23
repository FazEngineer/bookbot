from stats import get_word_count
from stats import get_character_number
from stats import chars_dict_to_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
   if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
   book_path = sys.argv[1]
   text = get_book_text(book_path)
   num_word = get_word_count(text)
   print(f"Found {num_word} total words") 
   print(get_character_number(text))
   char_dict = get_character_number(text)
   sorted = chars_dict_to_list(char_dict)

   for item in sorted:
       character = item["char"]
       if not character.isalpha():
           continue
       number = item["num"] 
       print(f"{character}: {number}")

main()

