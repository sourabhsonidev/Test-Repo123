
def sanitize_name(name):
    return ''.join(char for char in name if char.isalnum() or char.isspace())

def greet(name):
    safe_name = sanitize_name(name)
    if safe_name:
        print(f"Hello, {safe_name}!")
    else:
        print("Hello, guest!")

greet("Alice")
greet("Robert'); DROP TABLE Students;--")  # This will be sanitized
