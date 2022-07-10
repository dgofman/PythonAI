'''
4. Write code that does the following: opens the number_list.txt file that was created by the code you wrote in question 3, reads all of the numbers from the file and displays them, then closes the file.

>> python hw2_exercise4.py
2022-06-27 12:44:51.188 DEBUG: Open file: number_list.txt
2022-06-27 12:44:51.188 DEBUG: Read Context
2022-06-27 12:44:51.188 DEBUG: Close file: number_list.txt
  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19, 20
 21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39, 40
 41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59, 60
 61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79, 80
 81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99, 100

2022-06-27 12:44:51.190 DEBUG: Delete file: number_list.txt
2022-06-27 12:44:51.190 DEBUG: Open file: number_list.txt
  Error: [Errno 2] No such file or directory: 'number_list.txt'
None
'''

from file_manager import FileManager
from hw2_exercise3 import SaveNumbers

class ReadNumbers(FileManager):

    def __init__(self, filename):
        FileManager.__init__(self, filename)

def main():
    f = ReadNumbers(SaveNumbers.DEFAULT_FILE_NAME)
    print(f.read())
    f.delete()
    print(f.read())

if __name__ == "__main__":
    main()