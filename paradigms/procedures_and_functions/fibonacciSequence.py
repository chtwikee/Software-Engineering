#Result the number in the Fibonacci sequence
def fibonacciSequence(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fibonacciSequence(number - 1) + fibonacciSequence(number - 2)

# print(help(fibonacciSequence))