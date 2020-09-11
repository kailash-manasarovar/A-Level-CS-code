# Practice Papers Set 1 Paper 1 Q4
def convert_to_ascii(eb_value):

    if eb_value >= 193 and eb_value <= 201:
        return eb_value - 128

    elif eb_value >= 209 and eb_value <= 217:
        return eb_value - 135

    elif eb_value >= 226 and eb_value <=233:
        return eb_value - 143

    else:
        return -1


ascii_num = convert_to_ascii(209)
print(ascii_num)
print(chr(ascii_num))