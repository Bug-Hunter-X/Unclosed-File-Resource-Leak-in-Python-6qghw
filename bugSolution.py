def function_with_closed_file(filepath):
    try:
        with open(filepath, 'r') as file:
            # ... some code that processes the file ...
    except Exception as e:
        print(f"An error occurred: {e}")

# Calling the function using with statement
function_with_closed_file("my_file.txt")
