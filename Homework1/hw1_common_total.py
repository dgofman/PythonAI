class CommonTotal:
    def __init__(self, questions):
        self._values = self.__getValues(questions)

    def getSum(self):
        return sum(self._values)
    
    def __getValues(self, questions):
        index = 0
        total = len(questions)
        values = [None] * total
        
        while(index < total):
            try:
                values[index] = float(input(questions[index]))
                index += 1
            except Exception as e:
                print(f"\033[91m  Error: {e}\033[00m")
        return values