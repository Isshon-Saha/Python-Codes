import datetime

def main():
    uYear = input("Enter your birth year:")
    cYear = datetime.datetime.now().year
    Age = cYear - int(uYear)
    print("Your age is {}".format(Age))

if __name__ == '__main__': main()