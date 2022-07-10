'''
5. Write a function that accepts a string as an argument and returns true if the argument ends with the substring '.com'. Otherwise, the function should return false.

>> python hw2_exercise12.py

URL: http://www.google.com
is commercial domain:  True
URL: http://www.google.com/index.html
is commercial domain:  True
URL: https://www.cstu.edu/index.html
is commercial domain:  False
'''

def isCommercialDomain(url: str):
    print("URL:", url)
    return url.replace("//", "|").split("/")[0].endswith(".com")

def main():
    print("is commercial domain: ", isCommercialDomain("http://www.google.com"))
    print("is commercial domain: ", isCommercialDomain("http://www.google.com/index.html"))
    print("is commercial domain: ", isCommercialDomain("https://www.cstu.edu/index.html"))

if __name__ == "__main__":
    main()