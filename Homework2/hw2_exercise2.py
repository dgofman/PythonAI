'''
2. Write a program that opens the my_name.txt file that was created by the program in problem 1 reads your name from the file, displays the name on the screen, then closes the file.

>> python hw2_exercise2.py
2022-06-27 12:11:43.160 DEBUG: Open file: my_name.txt
2022-06-27 12:11:43.160 DEBUG: Read Context
2022-06-27 12:11:43.160 DEBUG: Close file: my_name.txt
David Gofman
2022-06-27 12:11:43.160 DEBUG: Delete file: my_name.txt
2022-06-27 12:11:43.161 DEBUG: Open file: my_name.txt
  Error: [Errno 2] No such file or directory: 'my_name.txt'
None
'''

from file_manager import FileManager
from hw2_exercise1 import WriteRecord

class ReadRecord(FileManager):

    def __init__(self, filename):
        FileManager.__init__(self, filename)

def main():
    f = ReadRecord(WriteRecord.DEFAULT_FILE_NAME)
    print(f.read())
    f.delete()
    print(f.read())

if __name__ == "__main__":
    main()