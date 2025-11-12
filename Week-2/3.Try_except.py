def divide_number(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            result = None
    except TypeError:
            print("Error: Inputs must be numbers!")
            result = None
    else:
            print(f"Division successful: {a} / {b} = {result}")
    finally:
            print("divide_numbers complete.\n")
    return result

def list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None
    except TypeError:
        print("Error: Invalid list or index type!")
        return None
    

def main():

    divide_number(10, 2)
    divide_number(10, 0)
    divide_number("10", 5)

    list = [1, 2, 3, 4]
    print("\nAccess list elements:")
    print(list_element(list, 2))
    print(list_element(list, 10))
    print(list_element("not a list", 1))


if __name__ == "__main__":
    main()