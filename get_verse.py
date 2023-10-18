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
def get_verse():
    
    print("\033[1m" + verse_me_ascii_art + "\033[0m")
    
    print("\033[1m" + "WELCOME TO VERSE ME!" + "\033[1m")
    
    
    while True:
        user_input = input("Do you want to search a verse? Type 'More' for more options (y/n): ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            search = input("Enter the book name, chapter and verse number: ")
            if search: 
                url = f"https://bible-api.com/"
        
                response = requests.get(f"{url}{search}")
        
                if response.status_code == 200:
                    json_data = response.json()
                    print(f"{found_it_ascii_art}")
            
            # Access verse details directly from the dictionary
                    book = json_data['reference']
                    text = json_data['text']
            
                    print(f"Book: {book} || Text: {text}")
            
                else: 
                    print(response.status_code, "Error")
                    
        elif user_input.lower() == "n" or user_input.lower() == "no":
            print("\033[1m" + bye_ascii_art + "\033[0m")
            break
        elif user_input.lower() == "more":
            print("\033[1m" + oprions_ascii_art + "\033[0m")
            print("1. Search for a verse")
            print("2. Random verse")
            print("3. Exit")
        elif user_input.lower() == "exit":
            print("\033[1m" + bye_ascii_art + "\033[0m")
            break
        elif user_input.lower() == "1":
            search = input("Enter the book name, chapter and verse number: ")
        elif user_input.lower() == "2":
            get_random_url = 'https://labs.bible.org/api/?passage=random&type=json&callback='
    
            response = requests.get(get_random_url)
    
            if response.status_code == 200:
                json_data = response.json()
                print(f"{found_it_ascii_art}")
        
                book = json_data[0]['bookname']
                chapter = json_data[0]['chapter']
                verse = json_data[0]['verse']
                text = json_data[0]['text']
        
                print(f"Book: {book} || {chapter}:{verse} || Text: {text}")
        
            else: 
                print(response.status_code,"Error")    
        elif user_input.lower() == "3":
            print("\033[1m" + bye_ascii_art + "\033[0m")
            break
        else:
            print("Invalid input. Press 'More' for more options")
            

get_verse()