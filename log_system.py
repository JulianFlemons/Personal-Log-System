import datetime
import json
import os 
DATA_DIR = '/data'
DATA_FILE = os.path.join(DATA_DIR, 'users_entries.json')
users_entries = []
#This allows the program to save the users journal entries in a json file. If the file does not exist, it will create a new one. If the file already exists, it will load the existing entries into the program. This way, the user can access their previous entries even after closing the program.
try:    
    with open(DATA_FILE, 'r') as f:
        users_entries = json.load(f)
except FileNotFoundError:
    pass 



def menu():
 # This is the main menu of the program. It will display the options for the user to choose from. The user can add an entry, view entries, delete an entry, or exit the program.   
    while True:
        print('Welcome to your personal log system!')
        print('=========================================')
        print('1. Add Entry')
        print('2. View Entries')
        print('3. Delete Entry')
        print('4. Exit')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Please enter a valid number.')
            continue
#This is the Add Entries Part of the project. Where The users will input there journal entry
        if choice == 1:
            print('Whats on your mind?')#Asks the user to input there journal entry. 
            journal_entry = input('> ') #Where the user will input there journal entry.
            #This is where the program will get the current date and time to save with the journal entry.
            entry_date = datetime.datetime.now()
            format_date = entry_date.strftime("%Y-%m-%d %H:%M:%S")
            #This is where the program will save the journal entry and the date it was created. It will save it as a dictionary with the keys "text" and "date". The value of "text" will be the journal entry and the value of "date" will be the date it was created. The program will then append the dictionary to the list of users entries.
            saved_entry = {"text" : journal_entry,
                           "date": format_date}
            users_entries.append(saved_entry)
            os.makedirs(DATA_DIR, exist_ok=True)
            with open(DATA_FILE, 'w') as f:
                json.dump(users_entries, f)
            print('Entry added successfully!')
            
#This is the View Entries Part of the project. Where The users will be able to view there journal entries
        elif choice == 2:
            print('Here are your previous entries:')
            #This is where the users will be able to view there journal entries. If they have no entries it will print a message saying they have no entries yet.
            if not users_entries:
                print('You have no entries yet.')
            else: 
                for entry in users_entries:
                    print(f"{entry['date']}: {entry['text']}")
                    
           
#This is the Delete Entries Part of the project. Where The users will be able to delete there journal entries
        elif choice == 3:
            print('Which entry would you like to delete?') #Asking the user which entry they would like to delete. 
            if not users_entries:
                print('You have no entries to delete')
            else:
                for i in users_entries: #Checking to see if the user has any entries to delete. 
                    print (f"{users_entries.index(i) + 1}. {i['date']}: {i['text']}")       
                try:
                    entry_number = int(input('Enter the number of the entry you want to delete: '))
                    if 1 <= entry_number <= len(users_entries):
                        users_entries.pop(entry_number - 1)
                        os.makedirs(DATA_DIR, exist_ok=True)
                        with open(DATA_FILE, 'w') as f:
                            json.dump(users_entries, f)
                        print('Entry deleted successfully!')
                    else:
                        print('Invalid entry number.')
                except ValueError:
                    print('Please enter a valid number.')

        
        
        
        elif choice == 4:
            print('Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')


menu()
