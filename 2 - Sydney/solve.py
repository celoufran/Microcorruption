# Replace the value of the variable hexvalues with the value determined from your challenge
hexvalues = "367c555c3b7a3052"
password = ''.join([(bytearray.fromhex(hexvalues).decode()[i:i+2])[::-1] for i in range(0, len(bytearray.fromhex(hexvalues).decode()), 2)])
print("The password is: ", password)