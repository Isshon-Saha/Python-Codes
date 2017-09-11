x=10

def sumandsub(n1,n2):
    x=11
    sum=n1+n2
    sub=n1-n2
    return [sum,x,sub]

def main():
    print("sum={} x={} sub={}".format(sumandsub(10,20)[0],sumandsub(10,20)[1],sumandsub(10,20)[2]))

if __name__ == '__main__':main()