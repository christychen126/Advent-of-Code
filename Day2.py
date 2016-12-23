import sys

def open_and_read_file(file_path):

    """Takes file path as string; returns text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #for files in sys.argv[1:]:
        # open(files).read()

    return open(file_path).read()


input_path = sys.argv[1]
input_text_1 = open_and_read_file(input_path)


