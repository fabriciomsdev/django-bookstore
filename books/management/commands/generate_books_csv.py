# Sample data to generate random books
from books.models import Book
from django.core.management.base import BaseCommand
import os
import csv
import random

import pandas as pd



class Command(BaseCommand):
    help = 'Load books from a CSV file into the database'

    def handle(self, *args, **kwargs):
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = current_path + '/fixtures/books.csv'

        titles = [
            "The Great Adventure", "Mystery of the Lost City", "Journey to the Unknown",
            "The Silent Whisper", "Secrets of the Ancient World", "Echoes of the Past",
            "The Final Frontier", "Voices in the Dark", "Dreams of the Future",
            "The Enchanted Forest", "Tales of the Brave", "Chronicles of Time",
            "The Forgotten Kingdom", "Shadows of the Night", "The Infinite Quest"
        ]

        authors = [
            "John Doe", "Jane Smith", "Emily Johnson", "Michael Brown",
            "Jessica White", "David Miller", "Sophia Davis", "James Wilson",
            "Olivia Moore", "William Taylor", "Isabella Anderson", "Benjamin Thomas",
            "Mia Harris", "Ethan Martin", "Ava Jackson", "Alexander Thompson",
            "Emma Garcia", "Mason Martinez", "Lucas Robinson", "Liam Clark"
        ]

        # Generate random data for 1000 books
        data = {
            "title": [random.choice(titles) + f" #{i}" for i in range(2000)],
            "author": [random.choice(authors) for _ in range(2000)],
        }

        # Convert to a DataFrame
        df = pd.DataFrame(data)

        # Save to CSV
        df.to_csv(file_path, index=False)

        self.stdout.write(self.style.SUCCESS("CSV file with 1000 books has been generated."))
