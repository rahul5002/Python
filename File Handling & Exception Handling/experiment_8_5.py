#Create multiple suitable exceptions for a file handling program.
class FileError(Exception):
    """Base class for custom file handling exceptions."""
    def __init__(self, filename, message="File handling error"):
        self.filename = filename
        super().__init__(f"{message}: {filename}")

def file_operation(filename, mode='r'):
    try:
        with open(filename, mode) as file:
            if mode == 'r':
                content = file.read()
                print(f"File read successful. First 50 chars: {content[:50]}")
                return content
            elif mode == 'w':
                file.write("Sample content")
                print("File written successfully")
    except FileNotFoundError:
        raise FileError(filename, "File not found")
    except PermissionError:
        raise FileError(filename, "Permission denied")
    except IOError as e:
        raise FileError(filename, f"IO Error: {str(e)}")
def main():
    try:
        filename = input("Enter filename: ")
        mode = input("Enter mode (r/w): ")
        if mode not in ['r', 'w']:
            print("Invalid mode. Use 'r' for read or 'w' for write.")
            return
        file_operation(filename, mode)
    except FileError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()