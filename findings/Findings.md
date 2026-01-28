# Findings

## General structure
To import a nam file devices requires 46 SYSEX MIDI messages
* message 0 has length 54 (bytes)
* messages 1-44 have length 380
* message 45 has length 350

Message 0 probably only describes a nam files is going to be loaded to the device and where it should be stored.

Messages 1-45 have the actual nam (snaptone) information.

### Messages structure
Each message has some bytes to describe what is the purpose of the messages and the actual data

#### Message 0

* 2 bytes for start and end sysex (first and last byte)
* 7 bytes to address GP-200 device
* ? bytes for instruction/command id
* ? rest of byte meaning
* 

#### Message 1-44
* 2 bytes for start and end sysex, first and last byte (0 and 379) or (0 and 349)
* 7 bytes to address GP-200 device (1 to 7)
* 3 bytes for instruction/command id (8 to 11)
* 2 bytes for message size or to describe the order or how many bytes have been sent already IDK.
 
14 bytes are used to describe what the data means, in total 366 data bytes

#### Message 45
Message 45 looks similar to messages 1-44, just with 336 data bytes


## Data
The data in each message appears to be split in hex digits to prevent coalitions with the MIDI SYSEX protocol.
so the actual data length is halved for 17124 hex digits (nibbles) to a total of 8220 bytes.

### NAM name
So far we found the NAM name to import the file is 16 character ascii string located in bytes [12, 28).