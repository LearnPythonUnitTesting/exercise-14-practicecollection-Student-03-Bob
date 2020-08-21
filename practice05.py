def fizzBuzz(i):
    type = 0
    if i % 3 == 0 or '3' in str(i):
        type += 3
    if i % 5 == 0 or '5' in str(i):
        type += 5
    if type == 3:
        return 'Fizz'
    elif type == 5:
        return 'Buzz'
    elif type == 8:
        return 'FizzBuzz'
    else:
        return str(i)
