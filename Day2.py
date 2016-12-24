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
input_text = open_and_read_file(input_path)
input_list = input_text.split('\n')

direction_dict = {
    "U" : [ -3, "456789"],
    "D" : [ 3, "123456"],
    "L" : [ -1, "235689"],
    "R" : [1, "124578"]
    }

def find_code(input_list):

    door_code = []
    starting_point = 5
    for code in input_list:

        for i in code:
            if str(starting_point) in direction_dict[i][1]:
                starting_point += direction_dict[i][0]
        door_code.append(starting_point)

    return door_code

print find_code(input_list)