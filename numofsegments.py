ipAddress =input("Please enter your IP Address: ")
ipAddress

segment = 1
segment_len = 0
char = ''

for char in ipAddress:
    if char == '.':
        print("segment {} has {} length".format(segment, segment_len))
        segment += 1
        segment_len = 0
    else:
        segment_len += 1
if char != '.':
    print("segment {} has {} length".format(segment, segment_len))






