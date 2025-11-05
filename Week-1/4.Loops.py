# Simple for loop
for i in range(5):
    print("Yo Yo: ", i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# Nested
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# While
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Nested while
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1