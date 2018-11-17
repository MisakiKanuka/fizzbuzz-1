number = int(input("1つの自然数を入れてね： "))

if number % 3 == 0:
    output = "Fizz"
elif number % 5 == 0:
    output = "Bazz"
else:
    output = str(number)

print(str(output))
