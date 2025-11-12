import functions as module  # importing your custom module

def main():

    print(module.greet_user("Boss"))

    numbers = [3, 6, 7]
    print("\nIndividual Calculations: ")
    print(f"Numbers: {numbers}")
    print(f"Sum: {module.add(*numbers)}")
    print(f"Product: {module.multiply(*numbers)}")
    print(f"Average: {module.average(*numbers)}")

    module.display_profile(Name="Parag Deb", Role="Developer", Language="Python")

    print("\nALl Calculations")
    summary = module.calculations(2, 4, 6, 8)
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
