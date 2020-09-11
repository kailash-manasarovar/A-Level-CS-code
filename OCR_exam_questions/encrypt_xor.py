# SAMPLE ASSESSMENT MATERIAL Paper 2 Q8
message = "111100001111" # input("Enter the message")...later
print(message)
key =  5 # input("Enter the key")...later

# get the length of the message
length_of_message = len(message)
# test
print(length_of_message)

# get the binary value of the key and eliminate the first two values
binary_key = bin(key)[2:]
# test
print(binary_key)
length_of_binary_key = len(binary_key)

# evalutate how many times to repeat the key
repeat = length_of_message // length_of_binary_key
# test
print(repeat)

# deal with the cases when there is a reminder
remainder = length_of_message % length_of_binary_key
print(remainder)
excess = ""
if remainder is not 0:
    excess = binary_key[0:remainder]
    print(excess)

# concatenate the encryption key
encryption_key = ""
for i in range(repeat):
    encryption_key += binary_key
encryption_key += excess
print(encryption_key)

# now we have
# input message
# key
# encryption key
# we can now do xor on input message and encryption key to get encrypted message
# go through the length of the messages and check if character at is equal

encrypted_message = ""
for i in range(len(message)):
    if message[i] == encryption_key[i]:
        encrypted_message += "0"
    else:
        encrypted_message += "1"
print(encrypted_message)

