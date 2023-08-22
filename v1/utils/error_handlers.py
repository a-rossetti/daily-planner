def handle_file_errors(func):
    # decorator to handle file-related errors
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"Error: File '{args[0].filename}' not found.")
        except IOError:
            print(f"Error: Unable to read/write the file '{args[0].filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return wrapper
