from django.core.management.base import BaseCommand
from api.models import Word

class Command(BaseCommand):
    help = 'Loads words into the database'

    def handle(self, *args, **kwargs):
        with open('api/words_alpha.txt', 'r') as f:
            for line in f:
                word = line.strip()
                Word.objects.create(word=word)
