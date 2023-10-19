import requests
verse_me_ascii_art = r"""

 _   _  _____ ______  _____  _____  ___  ___ _____ 
| | | ||  ___|| ___ \/  ___||  ___| |  \/  ||  ___|
| | | || |__  | |_/ /\ `--. | |__   | .  . || |__  
| | | ||  __| |    /  `--. \|  __|  | |\/| ||  __| 
\ \_/ /| |___ | |\ \ /\__/ /| |___  | |  | || |___ 
 \___/ \____/ \_| \_|\____/ \____/  \_|  |_/\____/ 
                                                   
"""

oprions_ascii_art = r"""


  ____  ___  ______________  _  ______
 / __ \/ _ \/_  __/  _/ __ \/ |/ / __/
/ /_/ / ___/ / / _/ // /_/ /    /\ \  
\____/_/    /_/ /___/\____/_/|_/___/  
                                      
"""

found_it_ascii_art = r"""

   _   _   _   _   _     _   _  
  / \ / \ / \ / \ / \   / \ / \ 
 ( F | O | U | N | D ) ( I | T )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ 

"""

bye_ascii_art = r"""

   _____  ______
  / _ ) \/ / __/
 / _  |\  / _/  
/____/ /_/___/  
                

"""
import requests

class VerseMe:
    def __init__(self):
        self.verse_me_ascii_art = verse_me_ascii_art
        self.found_it_ascii_art = found_it_ascii_art
        self.bye_ascii_art = bye_ascii_art
        self.options_ascii_art = oprions_ascii_art

    def get_verse(self):
        print("\033[1m" + self.verse_me_ascii_art + "\033[0m")
        print("\033[1m" + "WELCOME TO VERSE ME!" + "\033[1m" + "\n" + " Version 1.1")

        while True:
            user_input = input("Do you want to search a verse? Type 'More' for more options (y/n): ")
            if user_input.lower() in {"y", "yes"}:
                search = input("Enter the book name, chapter and verse number: ")
                if search:
                    self.search_and_display_verse(search)
                else:
                    print("Invalid input. Press 'More' for more options")
            elif user_input.lower() in {"n", "no"}:
                print("\033[1m" + self.bye_ascii_art + "\033[0m")
                break
            elif user_input.lower() == "more":
                self.display_options()
            else:
                print("Invalid input. Press 'More' for more options")

    def search_and_display_verse(self, search):
        url = f"https://bible-api.com/{search}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            print(f"{self.found_it_ascii_art}")

            book = json_data['reference']
            text = json_data['text']

            print(f"Book: {book} || Text: {text}")
        else:
            print(response.status_code, "Error")

    def display_options(self):
        print("\033[1m" + self.options_ascii_art + "\033[0m")
        print("1. Search for a verse")
        print("2. Random verse")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            search = input("Enter the book name, chapter and verse number: ")
            if search:
                self.search_and_display_verse(search)
            else:
                print("Invalid input. Press 'More' for more options")
        elif choice == "2":
            self.get_random_verse()
        elif choice == "3":
            print("\033[1m" + self.bye_ascii_art + "\033[0m")
            exit()
        else:
            print("Invalid choice. Please choose a valid option")

    def get_random_verse(self):
        get_random_url = 'https://labs.bible.org/api/?passage=random&type=json&callback='
        response = requests.get(get_random_url)

        if response.status_code == 200:
            json_data = response.json()
            print(f"{self.found_it_ascii_art}")

            book = json_data[0]['bookname']
            chapter = json_data[0]['chapter']
            verse = json_data[0]['verse']
            text = json_data[0]['text']

            print(f"Book: {book} || {chapter}:{verse} || Text: {text}")
        else:
            print(response.status_code, "Error")

if __name__ == "__main__":
    verse_me = VerseMe()
    verse_me.get_verse()