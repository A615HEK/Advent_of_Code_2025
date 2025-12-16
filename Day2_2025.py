# No change in puzzle input
input_file_path = "./Inputs/day1_input.txt"
with open(input_file_path) as input_file:
    input_file = input_file.readlines()
# Sample inputs before real test
input_file = ["R1000\n"]
# input_file = ["L68\n", "L30\n", "R48\n", "L5\n", "R60\n", "L55\n", "L1\n", "L99\n", "R14\n", "L82\n"]
current_num = 50
num_of_zeros = 0
for command in input_file:
    direction_to_turn = command[0]
    num_of_turns = int(command[1:-1])
    prev_num = current_num
    if direction_to_turn == "R":
        current_num = (current_num + num_of_turns)
    elif direction_to_turn == "L":
        current_num = (current_num - num_of_turns)
    if ((current_num < 0) and (prev_num>0)) or abs(current_num)>99:
        if abs(current_num) > 99:
            num_of_zeros += abs(current_num)//100
        else:
            num_of_zeros += 1
        if current_num%100 == 0:
            num_of_zeros -= 1
    # Get mod100 to bound value between 0 - 99
    current_num%=100
    if current_num == 0:
        num_of_zeros += 1
print(f"The answer is : {num_of_zeros}")
print(f"Current number is : {current_num}")
#  - Got it in da _ try!!!