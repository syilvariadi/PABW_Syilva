def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for i in range(1, 101):
    if is_even(i) == False:
        print(i)
    else:
        continue