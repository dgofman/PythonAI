'''
1. Input and output:

We put an end=' ' at the end of print line. This tells print to not end the line with a newline character and go to the next line.
print("How old are you?"')  # will add the newline

Write a code that will put the input and answers in the same line:

"How tall are you?"
"How much do you weigh?"

Now put show the answers in the following format:

So, you're ________(10 character wide, center)  old, __________(10 character wide, center)  tall and _________ (10 character wide, center) heavy."

>> python hw1_exercise1.py

<< How old are you? 18
<< How tall are you? 5.6 ft.
<< How much do you weigh? 150 lb 
<< So, you're     18      old,  5.6 ft.    tall and   150 lb   heavy.
'''

class Questionnaire:
    questions = (
        "How old are you? ",
        "How tall are you? ",
        "How much do you weigh? "
    )
    def __init__(self):
        self.answers = []

    def __str__(self):
        return "So, you're {:^10}  old, {:^10}  tall and {:^10} heavy.".format( *self.answers )

def main():
    q = Questionnaire()
    for question in q.questions:
        q.answers.append(input(question))
    print(q)

if __name__ == "__main__":
    main()