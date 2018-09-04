n = (input("Enter the length of the sequence: ")) # Do not change this line

x1 = 1
x2 = 2
x3 = 3
x4 = x1 + x2 + x3

counter = 0

while counter < n:
    if counter == 0:
        print(x1)
    elif counter == 1:
        print(x2)
    elif counter == 2:
        print(x3)
    elif counter == 3:
        print(x4)
    else:
        x1 = x2
        x2 = x3
        x3 = x4
        x4 = x1 + x2 + x3
        print(x4)
    counter += 1

