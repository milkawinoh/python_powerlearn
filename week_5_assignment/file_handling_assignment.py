try:
    # Writing to the file
    with open("my_file.txt", "w+") as file:
        lines = ["ilove coding\n", "123\n", "coding is fun\n", str(456) + "\n"]
        file.writelines(lines)
        file.seek(0)
        print("Contents after writing:")
        print(file.read())

    # Appending to the file
    with open("my_file.txt", "a+") as file:
        lines_to_append = ["i have appended first line\n", "second line\n", str(789) + "\n"]
        file.writelines(lines_to_append)
        print("\nContents after appending:")
        file.seek(0)
        print(file.read())

except FileNotFoundError as fnfe:
    print(f"File not found: {fnfe}")
except IOError as ioe:
    print(f"IO error: {ioe}")
except Exception as e:
    print(f"Error: {e}")
