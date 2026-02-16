from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def linebased(data, path):
    for line_number, line in enumerate(data, start=1):
        print(f"Line {line_number}: {line.strip()}")

    while True:
        try:
            # Loop through lines, allow user to modify a specific line
            choice = input("Enter number of line you want to change (or press 'q' to go back): ")

            if choice.lower() == 'q':
                print("Going back...")
                break

            index = int(choice) - 1

            if index < 0 or index >= len(data):
                print("Invalid choice.")
                continue

            print(data[index].strip())

            new_text = input("Type new text: ")
            data[index] = new_text + "\n"

            with open(path, 'w', encoding='utf-8') as f:
                for line in data:
                    f.write(line)

            print("Text updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

def wordbased(data, path):

    for line in data:
        print(line.strip())

    while True:
        try:
            word = input("Enter word to find (or press 'q' to go back): ")
            print()

            if word.lower() == 'q':
                print("Going back...")
                break

            count = 0
            for line in data:
                count += line.count(word)

            if count == 0:
                print("Word not found in file.")
                continue

            print(f"{count} occurrence(s) found.")

            new_word = input("Enter new word to replace it with: ")


            new_data = []
            for line in data:
                new_data.append(line.replace(word, new_word))

           
            with open(path, 'w', encoding='utf-8') as f:
                for line in new_data:
                    f.write(line)

            print("All occurrences replaced successfully.")
            break

        except Exception as e:
            print(f"Error: {e}")



def replace(file, path):

    data = file.readlines() # Read file content into list of lines

    while True:
        # Ask user to choose line-based or word-based editing
        try:
            program = input("Enter 1 for line-based Editing or Enter 2 for Word-based: ")
            program = int(program)
            if program == 1 or program == 2:
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print(f"Error: {e}")
    

    
    if program == 1:
        linebased(data, path)
    else:
        wordbased(data, path)
       





while True:
    print()
    user_path = input("Enter full file path (or 'q' to quit): ").strip()
    print()

    default_file = BASE_DIR / "input" / "data.txt"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = default_file
        if path.is_file():
            print(f"No path provided — using default file: {default_file.name}")
        else:
            print("No path provided and default file is missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_file() and path.suffix == ".txt":
        try:
            with path.open("r", encoding="utf-8") as file:
                print(f"File loaded successfully: {path.name}")
                replace(file, path)
        except Exception:
            print("Failed to open file.")
    else:
        print("Invalid file or file not found. Please check the path and try again.")