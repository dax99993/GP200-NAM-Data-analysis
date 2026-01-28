# GP200-NAM-Data-analysis
This project is for exploring and reverse engineer the GP-200 NAM import functionality.

The repository ohe data appears to be splitted in hex digits to prevent coalitions with the MIDI SYSEX protocol.
so the actual data length is halved for a total of 8220 bytes.
 consists of the following structure
* **exploration** folder containing scripts for exploring patterns in the midi data.
* **findings** folder to compile all the patterns found in the data, explaining their meaning and structures. 
* **src** folder contains the extracted data from the devices along with the nam files utilized to generate such data.
* **tests** folder contains scripts to test the patterns found and check they align with the captured midi messages.

Currently only one sample consisting of all midi messages for importing a NAM file to the DST module in the SnapTone position 1 is available.



