import os
import datetime
import glob

DIARY_FOLDER = "diary"

def get_diary_file(date):
    # Generate the filename for the given date
    filename = f"{date.strftime('%Y-%m-%d')}.txt"
    return os.path.join(DIARY_FOLDER, filename)

def add_story():
    # Prompt the user for the story content
    print("Enter your story for today (Press Enter on a new line to save):")
    story = ""
    while True:
        line = input()
        if line == "":
            break
        story += line + "\n"

    # Get the current date
    today = datetime.date.today()

    # Create the diary folder if it doesn't exist
    os.makedirs(DIARY_FOLDER, exist_ok=True)

    # Get the diary file for the current date
    diary_file = get_diary_file(today)

    # Save the story to the diary file
    with open(diary_file, "a") as f:
        f.write("=== Entry ===\n")
        f.write(story)
        f.write("=== End of Entry ===\n")

    print("Diary entry added.")

def view_story():
    # Prompt the user for the date to view entries
    print("Enter the date (YYYY-MM-DD) to view the diary entries:")
    date_str = input()

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    # Get the diary file for the specified date
    diary_file = get_diary_file(date)

    if os.path.exists(diary_file):
        # Read and display the diary entries for the specified date
        with open(diary_file, "r") as f:
            diary = f.read()
            print(diary)
    else:
        print("No diary entries found for the specified date.")

def search_story():
    # Prompt the user for the date to search entries
    print("Enter the date (YYYY-MM-DD) to search the diary entries:")
    date_str = input()

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    # Prompt the user for the keyword to search
    print("Enter the keyword to search in diary entries:")
    keyword = input().lower()

    matching_entries = []

    # Get the diary file for the specified date
    diary_file = get_diary_file(date)

    if os.path.exists(diary_file):
        # Read the diary file and search for the keyword
        with open(diary_file, "r") as f:
            entry = ""
            for line in f:
                if line == "=== Entry ===\n":
                    entry = ""
                elif line == "=== End of Entry ===\n":
                    if keyword in entry.lower():
                        matching_entries.append(entry)
                else:
                    entry += line

    # Display matching entries
    if matching_entries:
        print("Matching diary entries found:")
        for entry in matching_entries:
            print(entry)
    else:
        print("No matching diary entries found.")

def delete_story():
    # Prompt the user for the date to delete entries
    print("Enter the date (YYYY-MM-DD) to delete the diary entries:")
    date_str = input()

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    # Get the diary file for the specified date
    diary_file = get_diary_file(date)

    if os.path.exists(diary_file):
        # Delete the diary file
        os.remove(diary_file)
        print("Diary entries deleted.")
    else:
        print("No diary entries found for the specified date.")

def edit_story():
    # Prompt the user for the date to edit entries
    print("Enter the date (YYYY-MM-DD) to edit the diary entries:")
    date_str = input()

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        return

    # Get the diary file for the specified date
    diary_file = get_diary_file(date)

    if os.path.exists(diary_file):
        # Read the existing diary entries
        with open(diary_file, "r") as f:
            lines = f.readlines()
        
        # Prompt the user for the entry number to edit
        print("Enter the entry number you want to edit:")
        entry_number = int(input())

        entry_count = 0
        entry_start = 0
        entry_end = 0

        # Find the start and end indices of the entry to edit
        for i, line in enumerate(lines):
            if line == "=== Entry ===\n":
                entry_count += 1
                if entry_count == entry_number:
                    entry_start = i
            elif line == "=== End of Entry ===\n":
                if entry_count == entry_number:
                    entry_end = i
                    break

        # Retrieve the content of the entry to edit
        entry_content = "".join(lines[entry_start:entry_end+1])

        # Prompt the user for the new story content
        print("Enter the updated story (Press Enter on a new line to save):")
        new_story = ""
        while True:
            line = input()
            if line == "":
                break
            new_story += line + "\n"

        # Replace the old entry content with the new story content
        lines[entry_start:entry_end+1] = ["=== Entry ===\n", new_story, "=== End of Entry ===\n"]

        # Write the modified lines back to the diary file
        with open(diary_file, "w") as f:
            f.writelines(lines)

        print("Diary entry updated.")
    else:
        print("No diary entries found for the specified date.")

# Main program loop
while True:
    print("\nPersonal Diary Management\n")
    print("1. Add Story")
    print("2. View Story")
    print("3. Search Story")
    print("4. Delete Story")
    print("5. Edit Story")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_story()
    elif choice == "2":
        view_story()
    elif choice == "3":
        search_story()
    elif choice == "4":
        delete_story()
    elif choice == "5":
        edit_story()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")