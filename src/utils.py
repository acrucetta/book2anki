import openai

openai.api_key = "your_openai_api_key"


def get_book_content(book_title):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Please provide the content of the book titled '{book_title}'",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


book_title = "example_book"
book_content = get_book_content(book_title)
