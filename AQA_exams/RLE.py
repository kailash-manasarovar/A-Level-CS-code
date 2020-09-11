# test_string = "AAAGGGGHHHHHHH"
# track_count = 1
# track_letter = test_string[0]
#
#
# results = { track_letter : track_count }
#
#
# for i in range(1, len(test_string)):
#
#     if test_string[i] != test_string[i-1]:
#         track_count = 1
#         results[test_string[i]] = track_count
#
#     else:
#         track_count = track_count + 1
#         results[test_string[i]] = track_count
#
# print(results)


OT = "AAARRRRGGGHH"
NT = ""
FT = ""
count = 0
num = 0
first = OT[0]
for i in range(len(OT)):
    #try:
    first = OT[num]
    count = 0
    for k in range(len(OT)):
        if first == OT[k]:
            NT = first
            count += 1
    FT += NT + str(count)
    num += count
    #except:
    #    break

print(FT)



# test_string = "AAAGGGGHHHHHHH"
# count = 1
# previous_character = ""
# result_string = ""
#
# for character in test_string:
#     if character != previous_character:
#         # then we see the char for the first time, so we can set count to 1 and add it to the result
#         # first time this prints empty string
#         if count == 1:
#             result_string = result_string + previous_character  # IF count is 1 then only add the character
#             #print(result_string)
#         else:
#             # we go here only if count does not equal 1 so we reached the end of the group
#             result_string = result_string + previous_character  # this adds the new character
#             result_string = result_string + str(count)  # this adds the count value
#             # print(result_string)
#         count = 1  # count gets reset for new character here.
#         previous_character = character  # previous is now the character just looked at.
#     else:
#         count += 1
#
# else:  # This bit covers the final character in the loop.
#     if count == 1:  # Could be multiple of that final one so same check as above.
#         result_string = result_string + (character)
#     else:
#         result_string = result_string + str(count)
#         result_string = result_string + (character)
#
# print(result_string)