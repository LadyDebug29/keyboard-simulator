import random
import unicodedata


class Words:

    def __init__(self):
        super().__init__()
        self.words = []

    def download_words(self):
        chunk_size = 256
        read_bytes = 0
        with open('words', encoding="UTF-8") as f:
            while True:
                chunk = f.read(chunk_size)
                chunk_normalize = unicodedata.normalize('NFD', chunk)
                self.words.extend(chunk_normalize.split())
                if not chunk:
                    break
                read_bytes += len(chunk)

    def get_word(self):
        return random.choice(self.words)
