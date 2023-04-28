import csv


def save_anki_cards_to_csv(anki_cards, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow(["Question", "Answer"])
        for card in anki_cards:
            csv_writer.writerow(card)
