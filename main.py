from newClass import start


def main():
    a = start(Type="Bandor", Age=24)
    print("{} {}".format(a.getAge(), a.getType()))


if __name__ == '__main__': main()