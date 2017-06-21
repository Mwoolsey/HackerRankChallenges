# don't care how many are in each group since only the captian is alone
raw_input()
main_room_number_list = map(int, raw_input().split())

captians_room = None
room_number_count = {}

for room_number in main_room_number_list:
    if room_number in room_number_count:
        room_number_count[room_number] += 1
    else:
        room_number_count[room_number] = 1

for key, value in room_number_count.items():
    if value == 1 : captians_room = key

print captians_room
