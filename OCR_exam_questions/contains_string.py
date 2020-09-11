# Practice Papers Set 2 Paper 2 Q4b


def contains(string1, string2):
    if string1 == string2:
        return True
    elif len(string1) > len(string2):
        return False
    elif string1 in string2:
        return True
    else:
        return False


print(contains("fox", "foghound"))

