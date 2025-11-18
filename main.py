def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return
    except PermissionError:
        print("Error: You do not have permission to read this file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Create a new output filename
    new_filename = "modified_" + filename

    try:
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        print(f"File processed successfully! Saved as '{new_filename}'")
    except Exception as e:
        print(f"Could not write to file: {e}")


# Run the function
read_and_modify_file()