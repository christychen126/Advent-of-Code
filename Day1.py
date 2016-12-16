

"""Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away

R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5

"""

direction_string = "R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"

direction_list = direction_string.split(", ")

direction_dict = { 
                    "N": {"R": "E", "L": "W"},
                    "E": {"R": "S", "L": "N"},
                    "S": {"R": "W", "L": "E"},
                    "W": {"R": "N", "L": "S"}
                }

direction_block_dict = { 
                    "N": {"R": (1, 0), "L": (-1,0)},
                    "E": {"R": (0, -1), "L": (0,1)},
                    "S": {"R": (-1, 0), "L": (1,0)},
                    "W": {"R": (0, 1), "L": (0, -1)}
                }

def getdistance(direction_list):
    """get distance.

    >>> getdistance(["R2","L3"])
    5
    
    >>> getdistance(["R2","R2","R2"])
    2

    >>> getdistance(["R5", "L5", "R5", "R3"])
    12

    """
    #import pdb; pdb.set_trace()
    count_dict = {"N": 0, "E": 0, "S": 0, "W": 0}

    facing = "N"

    for direction in direction_list:
        turn = direction[0]
        block = int(direction[1:])
        facing = direction_dict[facing][turn]
        count_dict[facing] +=block

    distance = abs(count_dict["N"]-count_dict["S"]) + abs(count_dict["E"]-count_dict["W"])
    
    return distance

def get_location(direction_list):
    """get distance.

    >>> get_location(["R8", "R4", "R4", "R8"])
    4

    """

    location_list = [(0,0)]
    starting_location = (0,0)
    facing = "N"

    for direction in direction_list:
        turn = direction[0]
        block = int(direction[1:])
        for n in range(block):
            new_location = (starting_location[0]+ direction_block_dict[facing][turn][0],
                starting_location[1]+ direction_block_dict[facing][turn][1])
            if not new_location in location_list:
                location_list.append(new_location)
                starting_location=new_location
            else: 
                return abs(new_location[0]) + abs(new_location[1])
        facing = direction_dict[facing][turn]
                











