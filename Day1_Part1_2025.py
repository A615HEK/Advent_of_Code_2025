input_file_path = "./Inputs/day1_input.txt"
with open(input_file_path) as input_file:
    input_file = input_file.readlines()
# Sample inputs before real test
# input_file = ["L68\n", "L30\n", "R48\n", "L5\n", "R60\n", "L55\n", "L1\n", "L99\n", "R14\n", "L82\n"]
current_num = 50
num_of_zeros = 0
for command in input_file:
    direction_to_turn = command[0]
    num_of_turns = int(command[1:-1])
    # print(f"Direction: {direction_to_turn}, Turns: {num_of_turns}")
    if direction_to_turn == "R":
        # Add to the number and get the mod value to bound value between 0 - 99
        current_num = (current_num + num_of_turns)%100
        # print(f"R : {current_num}")
    elif direction_to_turn == "L":
        # Subtract from the number and get the mod value to bound value between 0 - 99
        current_num = (current_num - num_of_turns)%100
        # print(f"L : {current_num}")
    if current_num == 0:
        num_of_zeros += 1
print(f"The answer is : {num_of_zeros}")
# 1021 - Got it in da 1st try!!!