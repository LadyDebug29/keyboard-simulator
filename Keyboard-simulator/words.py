import os
import random
import loading_screen


class Words:

    def __init__(self):
        super().__init__()
        self.words = []

    def download_words(self):
        chunk_size = 256
        read_bytes = 0
        file_size = os.path.getsize('english_words')
        splash_screen = loading_screen.SplashScreen()
        splash_screen.show()
        with open('english_words') as f:
            while True:
                chunk = f.read(chunk_size)
                self.words.extend(chunk.split())
                if not chunk:
                    break
                read_bytes += len(chunk)
                splash_screen.progress_bar.setValue(int(read_bytes / file_size * 100))


    def get_word(self):
        return random.choice(self.words)
