def function_with_unclosed_file(filepath):
    try:
        file = open(filepath, 'r')
        # ... some code that processes the file ...
    except Exception as e:
        print(f"An error occurred: {e}")

# Calling the function without closing the file
function_with_unclosed_file("my_file.txt")