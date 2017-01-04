with open('input-Day7.txt') as inp:
    count_IP = 0
    for line in inp:
        line = line.strip()
        print line
        inside_bracket = False
        is_IP = False
        for index, char in enumerate(line):
            if index > 0 and index < len(line)-2:
                print index, char
                if char == "[":
                    inside_bracket = True
                if char == "]":
                    inside_bracket = False
                if char == line[index+1] and line[index-1] == line[index+2] and line[index-1] != char and not inside_bracket:
                    print char, line[index+1], line[index-1], line[index+2]
                    print "YESSSSSSS"
                    is_IP = True

                if char == line[index+1] and line[index-1] == line[index+2] and inside_bracket:
                    print char, line[index+1], line[index-1], line[index+2]
                    print "NO THIS IS NOT"
                    is_IP = False 
                    break
        if is_IP:
            print "IM GOING TO ADD ONE"
            count_IP += 1
            is_IP = False

print count_IP