file_version ="2.0"

def local_scope():
    local_var = "I am Parag"
    print("Inside function (local_scope):", local_var)

def global_scope():
    global file_version
    file_version = "3.0" 
    print("Inside function (global): file_version =", file_version)

def nonlocal_scope_example():
    message = "Outer message"

    def inner():
        nonlocal message
        message = "Modified by inner Parag"
        print("Inside inner():", message)

    inner()
    print("After inner():", message)

if __name__ == "__main__":
    
    print("1. Local Scope Example:")
    local_scope()
    
    print("\n2. Global Scope Example:")
    print("Before global_scope(), file_version =", file_version)
    global_scope()
    print("After global_scope(), file_version =", file_version)
    
    print("\n3. Nonlocal Scope Example:")
    nonlocal_scope_example()