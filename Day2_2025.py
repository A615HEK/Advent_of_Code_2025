input_file_path = "./Inputs/day2_input.txt"
with open(input_file_path) as input_file:
    input_file = input_file.readline()
    input_file = input_file.split(",")
# Sample inputs
# input_file = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224", "1698522-1698528", "446443-446449", "38593856-38593862","565653-565659", "824824821-824824827", "2121212118-2121212124"]
persistent_sum = 0
for input_range in input_file:
    underscore_index = input_range.index("-")
    start_id = input_range[:underscore_index]
    stop_id = input_range[underscore_index+1:]
    start_size_to_check, stop_size_to_check = 0, 0
    if len(start_id)%2 == 0:
        start_size_to_check = len(start_id)//2
    if len(stop_id)%2 == 0:
        stop_size_to_check = len(stop_id)//2
    if start_size_to_check:
        print("Yes to start size...")
        start_half = int(start_id[:start_size_to_check])
        start_checker = start_half+(start_half*(10**start_size_to_check))
        if int(start_id) < start_checker:
            start_id = start_checker
    elif 10**(len(start_id)) <= int(stop_id):
        print("New starters possible...")
        start_size_to_check = (len(start_id)//2)
        start_half = 10**(start_size_to_check)
        start_checker = start_half+(start_half*(10**(start_size_to_check+1)))
        start_size_to_check += 1
        if int(start_id) < start_checker:
            start_id = start_checker
    if not start_size_to_check:
        continue
    if stop_size_to_check:
        print("Yes to stop size...")
        stop_half = int(stop_id[:stop_size_to_check])
        stop_checker = stop_half+(stop_half*(10**stop_size_to_check))
        if int(stop_id) > stop_checker:
            stop_id = stop_checker
    print("Going to the loop...")
    print(f"IDs: {(start_id, stop_id)}")
    for num_to_be_checked in range(int(start_id), int(stop_id)+1):
        if int(str(num_to_be_checked)[:start_size_to_check])>start_half:
            start_half += 1
            start_size_to_check = len(str(start_half))
            start_checker = start_half+(start_half*(10**start_size_to_check))
        if num_to_be_checked == start_checker:
            print((num_to_be_checked, start_checker))
            persistent_sum += num_to_be_checked
print(persistent_sum)
# 56660955519 - Got it in da 1st try!!!