
def printNumbers(n):
    for i in range(n):
        print(2*i)

def triangle(n):

    for i in range(n):
        for j in range(i):
            print('*', end = "")

        print('')

printNumbers(10)
triangle(5)
