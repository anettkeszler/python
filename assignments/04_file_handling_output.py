"""
Reads and returns the entire contents of a file as a single string.
        1. Open and read the given file into a variable using the File read()
           function.
        2. Print the contents of the file.
        3. Return the contents of the file.
    Args:
        file_name (str): Name of the file to be read.
    Returns:
        str: Entire contents of the file.
"""
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        return data
    

"""
Reads a file and returns a list where each element is a line in the file.
        1. Open the given file.
        2. Read the file line-by-line and append each line to a list.
        3. Return the list.
    Args:
        file_name (str): Name of the file to be read.
    Returns:
        list: List where each item is a line from the file.
"""
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        return data
        

"""
Writes the first line of a given string to an output file.
        1. Get the first line of file_contents.
        2. Use the File write() function to write the first line into a file
           with the name from output_filename.
        The first line is everything in a string before the first newline ('\n') character.
    Args:
        file_contents (str): String containing multiple lines of text.
        output_filename (str): Name of the file to write the first line into.
"""
def write_first_line_to_file(file_contents:str, output_filename):
    with open(output_filename, 'w') as file:
        file.write(file_contents.split("\n")[0])


def main():
    file_name = "assignments/04_sampletext.txt"

    print("Exercise 1:")
    print(read_file(file_name))

    print("Exercise 2:")
    print(read_file_into_list(file_name))


    print("Exercise 3:")
    file_contents = read_file(file_name)

    write_first_line_to_file(file_contents, "assignments/04_output.txt")


if __name__ == "__main__":
    main()