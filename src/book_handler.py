from typing import List
import openai
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    chapters: List[int] = []


def get_book_content(book_title) -> str:
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Please provide the content of the book titled '{book_title}'",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def list_book_chapters(book_title) -> str:
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Please list the chapters of the book titled '{book_title}'",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def get_anki_cards(chapter: int) -> str:
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Generate the anki cards for chapter {chapter}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
