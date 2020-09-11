# 2017 Paper 1 June Q10
def validate_answer(answer, random_letters):
    i=0
    score = 0
    while i<len(answer):
        j=0
        letter = answer[i]
        #print(letter)

        while j < 10:

            if random_letters[j] == letter:
               score = score + 1

            j=j+1

        i=i+1

    return score

random_letters = "OPXCMURETN"
answer = "COMPUTER"

print(validate_answer(answer, random_letters))