import requests
import json 
import random

from ascii import verse_me_ascii_art, oprions_ascii_art, found_it_ascii_art, bye_ascii_art
from security import safe_requests

class VerseMe:
    def __init__(self):
        self.verse_me_ascii_art = verse_me_ascii_art
        self.found_it_ascii_art = found_it_ascii_art
        self.bye_ascii_art = bye_ascii_art
        self.options_ascii_art = oprions_ascii_art

    def get_verse(self):
        print("\033[1m" + self.verse_me_ascii_art + "\033[0m")
        print("\033[1m" + "WELCOME TO VERSE ME!" + "\033[1m" + "\n" + " Version 1.2")

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
        response = safe_requests.get(url)

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
        print("3. Feeling the need for more?")
        print("4. Exit")
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
            VerseMe.Verse_mood().order_verse()
        elif choice == "4":
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

    class Verse_mood:
        def __init__(self):
            pass
            
        def order_verse(self):
            
            print("\033[1m" + "How are you feeling today?" + "\033[0m")
            
            print("\033[1m" + "1. Anger" + "\033[0m")
            print("\033[1m" + "2. Patience" + "\033[0m")
            print("\033[1m" + "3. Motivation" + "\033[0m")
            print("\033[1m" + "4. Depression" + "\033[0m")
            print("\033[1m" + "5. Upsmanship" + "\033[0m")
            print("\033[1m" + "6. Love" + "\033[0m")
            print("\033[1m" + "7. Obedience" + "\033[0m")
            
            choice = input("Enter your choice: ")
            
            if choice == "1" or choice == "Anger":
                
                self.anger_verse()
                    
            elif choice == "2" or choice == "Patience":

                self.patience_verse()
                    
            elif choice == "3" or choice == "Motivation":
                
                self.motivation_verse()
                    
            elif choice == "4" or choice == "Depression":
                
                self.depression_verse()
                    
            elif choice == "5" or choice == "Uplifting":
                
                self.uplift_verse()
                    
            elif choice == "6" or choice == "Love":
               
                self.love_verse()
                    
            elif choice == "7" or choice == "Obedience":
                
                self.obedience_verse()
                    
            else:
                
                print("Invalid choice. Please choose a valid option")
                
        def anger_verse(self):
            file_name = "verse_mood/data/data_verse_anger.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
            
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
                
        def patience_verse(self):
            file_name = "verse_mood/data/data_verse_patience.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
                
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
                
        def motivation_verse(self):
            file_name = "verse_mood/data/data_verse_motivation.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
                
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
                
        def depression_verse(self):
            file_name = "verse_mood/data/data_verse_depression.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
                
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
        
        def uplift_verse(self):
            file_name = "verse_mood/data/data_verse_uplifting.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
                
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
                
        def love_verse(self):
            file_name = "verse_mood/data/data_verse_love.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
                
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])
                
        def obedience_verse(self):
            file_name = "verse_mood/data/data_verse_obedience.json"
            
            with open(file_name, 'r') as f:
                verses = json.load(f)
            
            random_choice = random.choice(verses)
            
            print("Verse: " + random_choice['verse'])
            print("Reference: " + random_choice['reference'])

if __name__ == "__main__":
    verse_me = VerseMe()
    verse_me.get_verse()
