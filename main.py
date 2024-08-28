def main():

    """using with methode and open function to open a filepath in quotes, save it as f, and using the .read methode to read the file and assign it to
    file_content """

    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"{count_of_words(text)} words where found in the document at the path \"{book_path}\"")

def get_book_text(path):

    
    with open(path) as f:
        return f.read()
        #print(file_content)


def count_of_words(text):
    words = text.split()
    return len(words)
        


main()