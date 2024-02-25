# Part a
print("a. Counting in 10s from 0 to 100:", end=' ')
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Part b
print("b. Counting down from 20 to 1:", end=' ')
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part c
num_stars = int(input("c. Enter the number of stars: "))
print("*" * num_stars)

# Part d
num_stars_lines = int(input("d. Enter the number of lines for increasing stars: "))
for i in range(1, num_stars_lines + 1):
    print("*" * i)
