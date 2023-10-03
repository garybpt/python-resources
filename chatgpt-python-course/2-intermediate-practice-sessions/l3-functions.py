def calculate_sum(sum1, sum2):
    return sum1 + sum2

sum1 = input("What is the first value? ")
sum1 = int(sum1)

sum2 = input("What is the second value? ")
sum2 = int(sum2)

total = calculate_sum(sum1, sum2)

print("The total is: ", total)