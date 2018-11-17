def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

        return str(number)

result = fizzbuzz_convert(1)
print(result)  # 1

fizzbuzz_convert(2)
fizzbuzz_convert(3)
fizzbuzz_convert(4)
fizzbuzz_convert(5)
fizzbuzz_convert(6)
fizzbuzz_convert(15)
fizzbuzz_convert(100)
