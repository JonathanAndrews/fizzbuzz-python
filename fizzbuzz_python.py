
def fizzer(number):
    if is_divisible_by(number, 3):
        return "Fizz"
    return number

def buzzer(number):
    if is_divisible_by(number, 5):
        return "Buzz"
    return number

def fizzbuzzer(number):
    if is_divisible_by(number, 15):
        return "Fizzbuzz"
    return number

def is_divisible_by(number, divisor):
    return number % divisor == 0
