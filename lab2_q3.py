num = int(input("Please enter a number between 3 and 9: "))

# First loop for the top half of the pattern
for i in range(1, num+1):
    print('*' * i)
    if i == num:
        # Second loop for the bottom half of the pattern
        for j in range(num-1, 0, -1):
            print('*' * j)