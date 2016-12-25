import sys


def parsing_input(file_path):

    input_text = open(file_path).read()
    input_list = input_text.split('\n')
    new_input_list = []

    for string in input_list: 
        string = string.split()
        string = [int(num) for num in string]
        new_input_list.append(string)
        
    return new_input_list

input_list = parsing_input(sys.argv[1])



def check_triangle(input_list):

    triangle_count = 0
    for triangle in input_list:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            triangle_count += 1

    return triangle_count

print check_triangle(input_list)