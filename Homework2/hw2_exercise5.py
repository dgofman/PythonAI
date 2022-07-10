'''
1. Personal Web Page Generator
Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen:
Enter your name: Julie Taylor
Describe yourself: I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app developer after I graduate.
Once the user has entered the requested input, the program should create an HTML file, containing the input, for a simple Web page. Here is an example of the HTML content.

>> python hw2_exercise5.py
Enter your name: Julie Taylor
Describe yourself: I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app developer after I graduate.
2022-06-27 13:26:50.101 DEBUG: Open file: about.html
2022-06-27 13:26:50.102 DEBUG: Write: 
<html>
<head>
</head>
<body>
    <center>
        <h1>Julie Taylor</h1>
    </center>
    <hr />
    I am a computer science major, a member of the Jazz club, and I hope to work as a mobile app developer after I graduate.
    <hr />
</body>
</html>

2022-06-27 13:26:50.103 DEBUG: Close file: about.html
'''

import time
import webbrowser
from file_manager import FileManager

class HTMLGenerator(FileManager):
    DEFAULT_FILE_NAME = "about.html"
    __TEMPLATE = """
<html>
<head>
</head>
<body>
    <center>
        <h1>{}</h1>
    </center>
    <hr />
    {}
    <hr />
</body>
</html>
    """
    def __init__(self, filename):
        FileManager.__init__(self, filename)

    def generate(self):
        self.write(self.__TEMPLATE.format(
            input("Enter your name: "),
            input("Describe yourself: ")
        ))

def main():
    f = HTMLGenerator(HTMLGenerator.DEFAULT_FILE_NAME)
    f.generate()
    webbrowser.open(HTMLGenerator.DEFAULT_FILE_NAME)
    time.sleep(3) # delay opening file in browser before deleting
    f.delete()

if __name__ == "__main__":
    main()