'''
3. Write code that does the following: opens an output file with the filename number_list.txt, uses a loop to write the numbers 1 through 100 to the file, then closes the file.

>> python hw2_exercise3.py
2022-06-27 12:27:20.525 DEBUG: Open file: number_list.txt
2022-06-27 12:27:20.526 DEBUG: Close file: number_list.txt
'''

from file_manager import FileManager

class SaveNumbers(FileManager):
    DEFAULT_FILE_NAME = "number_list.txt"

    def __init__(self, filename):
        FileManager.__init__(self, filename)

def main():
    f = SaveNumbers(SaveNumbers.DEFAULT_FILE_NAME)
    for i in range(1, 100 + 1):
        if (i % 20 == 0):
            f.append("{}\n".format(i))
        else:
            f.append("{:>3}, ".format(i))
    f.close()

if __name__ == "__main__":
    main()