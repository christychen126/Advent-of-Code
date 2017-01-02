import sys
import operator

def parsing_input(file_path):

    input_text = open(file_path).read()
    input_list = input_text.split('\n')
    

    return input_list

input_list = parsing_input(sys.argv[1])


def find_code(input_list):

    dic0 = {}
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    dic5 = {}
    dic6 = {}
    dic7 = {}

    for n in input_list:
        for index, char in enumerate(n):
            find_dict = "dic"+ str(index)
            find_dict = eval(find_dict)
            find_dict[char] = find_dict.get(char,0)+1


    index0 = min(dic0.iteritems(), key=operator.itemgetter(1))[0]
    index1 = min(dic1.iteritems(), key=operator.itemgetter(1))[0]
    index2 = min(dic2.iteritems(), key=operator.itemgetter(1))[0]
    index3 = min(dic3.iteritems(), key=operator.itemgetter(1))[0]
    index4 = min(dic4.iteritems(), key=operator.itemgetter(1))[0]
    index5 = min(dic5.iteritems(), key=operator.itemgetter(1))[0]
    index6 = min(dic6.iteritems(), key=operator.itemgetter(1))[0]
    index7 = min(dic7.iteritems(), key=operator.itemgetter(1))[0]

    return index0+index1+index2+index3+index4+index5+index6+index7


print find_code(input_list)