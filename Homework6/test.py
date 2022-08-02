import re
import PyPDF2

def parse(filname):
    f = open(filname, "r", encoding="utf-16")
    content = f.read()
    f.close()
    sections = content.split("\n\n")

    arr = re.sub(r"word --\s+", "", sections[0])
    arr = re.split(r"\n|\s+-- frequency: ", arr)
    words1 = {}
    for i in range(0, len(arr), 2):
        try:
            words1[arr[i]] = int(arr[i + 1]) 
        except ValueError:
            continue

    arr = re.split(r"\s\s+|\s|\n", sections[1])
    words2 = {}
    for i in range(0, len(arr), 2):
        try:
            words2[arr[i]] = int(arr[i + 1]) 
        except:
            continue
    return words1, words2

def main():
    wordList = set()
    pdfFileObj = open("SampleCh7.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(4):
        pageObj = pdfReader.getPage(i)
        # extracting the words from page.into database using just regular expressions
        wordList |= set(re.split(r"\s|\n|\(|\)|\.|\,|\-|\–|\/|\?", re.sub(":", "", re.sub("’", "'", pageObj.extractText().lower()))))

    #parse my output file
    words1, words2 = parse("my_output.txt")
    
    complexWords = {"person": "people", "satisfy": "satisfies", "ll": "'ll"} # match words in plural
    posfixes = ("", "s", "'s", "es") # plural ending
    #verify missing keywords in PDF file
    for key in words2.keys():
        exists = False
        for posfix in posfixes:
            if key in complexWords or key + posfix in wordList:
                exists = True
                break
        if not exists:
            print("Missing PDF key:", key)

    #parse Glen's output file
    words3, words4 = parse("qin790_output.txt")

    #compare my keys agains Glen's output
    for key in words1.keys():
        if key in words3:
            if words1[key] != words3[key]:
                print("1. Number of frequencies: (mine)", words1[key], "Glen's:", words3[key])
            words3.pop(key)
        else:
            print("2. Missing key in Glen's output file:", key)

    print()
    for key in words3.keys():
        print("3. Missing key in my output file:", key)

    for key in words2.keys():
        if key in words4:
            if words2[key] != words4[key]:
                print("4. Number of frequencies: (mine)", words2[key], "Glen's:", words4[key])
            words4.pop(key)
        else:
            print("5. Missing key in Glen's output file:", key)

    print()
    for key in words4.keys():
        print("6. Missing key in my output file:", key)


if __name__ == "__main__":
    main()