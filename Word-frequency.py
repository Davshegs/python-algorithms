"""
A program that iterate through a given text file and return the individual words present and their
individual number of occurance 

"""
# Import the necessary functionality
from collections import Counter
import re

# create a function that reads text file 
def read_text(file):
    with open(file, 'r') as text_file:
        opened_text = text_file.read()

    return opened_text

# Create a function that finds and counts all the words present in the text
def get_frequency(file: str) -> list[tuple[str, int]]:
    # lower case all the words to avoid case insensitivity
    opened_text = read_text(file)
    lowered_text: str = opened_text.lower()

    # Use regular expression to find all words, including those with apostrophes or hyphens
    words: str = re.findall(r"\b\w+['.-]?\w*\b", lowered_text)

    # Count the occurrences of each word
    word_counts: Counter = Counter(words)

    # return the most common word
    return word_counts.most_common()


# create an entry point
def main() -> None:
    # get user input
    try:
        file: str = input('Enter the text: ').strip()

        word_frequency: list[tuple[str, int]] = get_frequency(file)

        # format the way your output appears 
        for word, count in word_frequency:
            print(f'{word} : {count}')
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')

#run script
if __name__ == '__main__':
    main()