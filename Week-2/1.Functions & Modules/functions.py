file_name = "Functions & Modules"

def greet_user(name="User"):
    return f"Hello {name}, welcome to {file_name}!"

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculations(*nums):
    return {
        "Sum": add(*nums),
        "Product": multiply(*nums),
        "Average": average(*nums)
    }

def display_profile(**info):
    print("\nInformation: ")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")

def demo():
    print(greet_user("Boss"))
    print("\nAll Calculations: ", calculations(10, 20, 30, 40))
    display_profile(Name="Parag Deb", Role="Developer", Language="Python")

if __name__ == "__main__": #run demo , when directly executed
    demo()