"""
3.2.5 - Read file exception handling with try-except-else-finally
Added decorator for fun
"""
import pathlib


def content_print(fn):
    def wrapper(*args, **kwargs):
        print(f"{'FILE READ START':_^30}")
        fn(*args, **kwargs)
        print(f"{'FILE READ END':_^30}\n")
    return wrapper


@content_print
def read_file(file_name):
    if pathlib.Path(file_name).exists():
        try:
            # purposefuly not using 'with open' to practice try block
            f = open(file_name, 'r')
        except IOError as e:
            print(e("Trouble reading file"))
        else:
            [print(line) for line in f.read().splitlines()]
        finally:
            f.close()
    else:
        print("File does not exist")


def main():
    read_file("nextpy3.2.txt")  # File which exists
    read_file("IMAGINARY FILE.txt")  # File which does not exist


if __name__ == "__main__":
    main()
