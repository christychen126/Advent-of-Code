import sys
import operator

def parsing_input(file_path):

    input_text = open(file_path).read()
    input_list = input_text.split('\n')
    new_input_list = []

    for string in input_list: 
        key = string[-6:-1]
        ids = int(string[-10:-7])
        chars = string[:-11]
        new_input_list.append([key, ids, chars])

    return new_input_list



def check_real_room(room_list):

    id_sum = 0

    for room in room_list:
        char_dict = {}
        for char in room[2]:
            if char != "-":
                char_dict[char] = char_dict.get(char, 0) + 1
        top_five = [item[0] for item in sorted(char_dict.iteritems(), key=lambda(k, v): (-v, k))][0:5]
        
        is_real_room = True

        for n in range(5):
            if room[0][n] != top_five[n]:
                is_real_room = False
        if is_real_room is True:
            id_sum += room[1]

    return id_sum

room_list = parsing_input(sys.argv[1])
# print check_real_room(room_list)



def get_room_name(room_list):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for room in room_list:
     
        room_name = ''
        shift_num = room[1] % 26
        
        for char in room[2]:
            
            if char == "-":
                room_name += " "
            else:     
                new_index = alphabet.index(char) + shift_num
                if new_index > 25:
                    new_index -= 26

                room_name += alphabet[new_index]


        print room_name, room[1]


get_room_name(room_list)







