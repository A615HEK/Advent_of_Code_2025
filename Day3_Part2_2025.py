input_file_path = "./Inputs/day3_input.txt"
with open(input_file_path) as input_file:
    input_file = input_file.readlines()
# Sample inputs
# input_file = ["987654321111111\n","811111111111119\n","234234234234278\n","818181911112111\n"]
total_capacity = 0
for battery_pack in input_file:
    bigger_battery = int(battery_pack[0])
    smaller_battery = int(battery_pack[1])
    for battery_num in range(1, len(battery_pack)-1):
        battery = int(battery_pack[battery_num])
        if battery > bigger_battery and (battery_pack[battery_num+1].isnumeric()):
            bigger_battery = battery
            smaller_battery = int(battery_pack[battery_num+1])
        elif battery > smaller_battery:
            smaller_battery = battery
    battery_value = (bigger_battery*10 + smaller_battery)
    print(battery_value)
    total_capacity += battery_value
print(f"Total output: {total_capacity}")
# 17166 - Got it in da 1st try!!!