# 2017 Paper 1 Question 7
def check_access(given_password, password_hash, locked):

    # FIRST STEP : get the hash of the password the user entered
    hashed_user_input = hash(given_password)

    # SECOND STEP : set a variable that we will use as a result
    allowed_in = False

    # THIRD STEP : check to see if the hashed input is the same as the password_hash we got from database (done outside the question)
    if hashed_user_input == password_hash:
        allowed_in = True

    # FOURTH STEP : check is locked is set to 1 or 0
    if locked == 1:
        allowed_in = False

    # FINAL STEP : return whether or not the user is allowed in
    return allowed_in



# test the code
# set user input
given_password = "Let me in!"

# we just do this to test it, in reality, we get this value from the database
correct_password_hash = hash(given_password)

# let's test an incorrect one
incorrect_password_hash = "kjskjk4ufoiuowiud"

# with this value we can test the locked, 1 or 2
locked = 0

print(check_access(given_password, incorrect_password_hash, locked))





