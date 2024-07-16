notes = {}

def create_note():
    title = input("Enter the title for your note: ")
    content = input("Enter the content of your note: ")
    notes[title] = content
    print("Note created successfully!")

def view_notes():
    if not notes:
        print("No notes to display.")
    else:
        print("Your notes:")
        for title, content in notes.items():
            print(f"Title: {title}\nContent: {content}\n")

def edit_note():
    title = input("Enter the title of the note you want to edit: ")
    if title in notes:
        new_content = input("Enter the new content for the note: ")
        notes[title] = new_content
        print("Note edited successfully!")
    else:
        print("Note does not exist.")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a new note")
        print("2. View existing notes")
        print("3. Edit a note")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2 or 3).")

main()