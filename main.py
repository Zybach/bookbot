def main():

    """using with methode and open function to open a filepath in quotes, save it as f, and using the .read methode to read the file and assign it to
    file_content """

    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):

    
    with open(path) as f:
        return f.read()
        #print(file_content)



main()