import openai
from prompts import OUTPUT_FILE_NAME, GET_BOOK_CHAPTERS, OPEN_AI_API_KEY
from book_handler import list_book_chapters


def main():
    # Connect to the OpenAI API
    openai.api_key = "OPEN_AI_API_KEY"
    models = openai.Model.list()

    # Get the book title from the user
    book_title = input("Please enter the title of the book: ")

    # Get the book chapters calling the OpenAI API
    book_chapters = list_book_chapters(book_title)

    return book_chapters


if "__name__" == "__main__":
    print("Hello World!")
