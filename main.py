def main():

	# Example Hex Value:  00 FA080001013CBCCCC34C8053132333435

	#                                   HEX ENCODED NUMBER
	#  Protocol   Identifier    UUI Data Length       UUI Data               2nd Protocol      Metadata Length         MetaData
	#  (1 Byte)    (1 Byte)       (1 Byte)                                    (1 Byte)            (1 Byte)
	#     00          FA             08            0001013CBCCCC34               C8                  05               3132333435

	encodedUUI = "04C80B31303030303B313B323B34FA08001502A15F749DE8"

	decodedUUI = ""

	if encodedUUI != "":
		try:
			uuiBytes = ""
			# Code to be place here

			# Result
			# uuiBytes = bytes.fromhex(encodedUUI)
			#
			# decodedUUI = uuiBytes[3:14].decode()


		except Exception as e:
			print("Unable to decode UUI string " + str(e));

	else:
		print("Nothing to decode ");

	print(40*"-"+"\ndecodedUUI is           " + str(decodedUUI));
	print("UUI output we expect is " + "10000;1;2;4\n"+40*"-");

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

