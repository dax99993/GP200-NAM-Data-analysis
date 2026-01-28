from src.data.midi_messages import dst1_nam_capture_msgs

nam_name = "APP-6505Plus-MidForward-Gain-01"
msgs = dst1_nam_capture.ds1_import_messages

# Explore general structure
n_msgs = len(msgs)

# Only first (54) and last msg (350) have different size all other are 380 bytes
msgs_len = [len(msg) for msg in msgs]
n_data_bytes = sum(msgs_len)

print(f"To import a NAM file {n_msgs} MIDI SYSEX messages are required")
print(f"Split in messages of size\n{msgs_len}")
print(f"For a total of {n_data_bytes} bytes")


print(msgs[0])
print(msgs[1])
print(msgs[2])
print(msgs[-2])
print(msgs[-1])

# Probably message 0 just instructs the device a nam files is going to be imported and where it will be stored.
# 2 bytes for start and end sysex (first and last byte)
# 7 bytes to address GP-200 device
# ? bytes for instruction/command id
#

# I think for messages 1 to 44 the sysex header has size 13
# 2 bytes for start and end sysex, first and last byte (0 and 379) or (0 and 349)
# 7 bytes to address GP-200 device (1 to 7)
# 3 bytes for instruction/command id (8 to 11)
# 2 bytes for message size or to describe the order or how many bytes have been sent already IDK.
# So 14 bytes are used to describe what the data means, in total 366 data bytes
msgs_size = [int.from_bytes(msg[11:13], byteorder='little', signed=False) for msg in msgs[1:]]
print(msgs_size)
print([msgs_size[i+1] - msgs_size[i] for i in range(len(msgs_size) - 1)])

# I think message 45 is similar to messages 1 to 44, just with 336 data bytes

# Lets explore the actual data

# Message 0

# Message 1 to 45
# Remove the 14 bytes
data_msgs_bytes = [msg[13:-1] for msg in msgs[1:]]
data_msgs_total_bytes = [len(msg) for msg in data_msgs_bytes]

# print(data_msgs_bytes[1])
# print(data_msg_total_bytes)

# I think the bytes are hex digits split to prevent coalition with midi sysex protocol
# So the data information is actually halved!
map_hex_digits = lambda high_nibble, low_nibble: (high_nibble<<4) | low_nibble
data_msgs = []
for msg in data_msgs_bytes:
    data = [map_hex_digits(msg[i], msg[i+1]) for i in range(0, len(msg) - 1, 2)]
    data_msgs.append(data)

print(len(data_msgs_bytes), len(data_msgs_bytes[0]), data_msgs_bytes[0])
print(len(data_msgs), len(data_msgs[0]), data_msgs[0])
n_data_bytes = sum(len(msg) for msg in data_msgs)
print("Total data bytes", n_data_bytes)

