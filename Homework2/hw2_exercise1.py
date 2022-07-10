'''
1. Write a program that opens an output file with the filename my_name.txt, writes your name to the file, then closes the file.

>> python hw2_exercise1.py
2022-06-27 12:01:06.735 DEBUG: Open file: my_name.txt
2022-06-27 12:01:06.737 DEBUG: Write: David Gofman
2022-06-27 12:01:06.737 DEBUG: Close file: my_name.txt
'''

from file_manager import FileManager

class WriteRecord(FileManager):
    DEFAULT_FILE_NAME = "my_name.txt"

    def __init__(self, filename):
        FileManager.__init__(self, filename)

def main():
    f = WriteRecord(WriteRecord.DEFAULT_FILE_NAME)
    f.write("David Gofman")

if __name__ == "__main__":
    main()