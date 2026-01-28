from midi_message_general_structure import nam_name, data_msgs

# Flatten all data
data = [b for msg in data_msgs for b in msg]

# Let's convert the data bytes to ascii and see if what info can we find
data_ascii = ''.join(map(chr, data))
print(data_ascii)
# Can only see the nam name

# Let's find the nam name byte positions
# Device only allows for 16 character name
max_character_len = 16
nam_name = nam_name[:max_character_len]
print("Device NAM name", nam_name)

# NAM name is found from index 12 to index 12+16 -1 = 27
# NAM name [12, 28)
idx = data_ascii.find(nam_name)
print(idx, data_ascii[idx:idx+max_character_len])
