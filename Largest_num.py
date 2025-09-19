def is_even(number):
    return number % 2 == 0

numbers = []
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    numbers.append(num)

    largest = max(numbers)
    print(largest)


