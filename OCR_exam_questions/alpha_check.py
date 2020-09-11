# FUNCTION is_in_order(word)
# IF LENGTH(word) = 1 THEN
#   RETURN TRUE
# ELSE
#   first_char = first character in word
#   rest_of_word = all characters in word except the first
#   IF first_char > rest_of_word THEN
#       RETURN FALSE
#   ELSE
#       RETURN is_in_order(rest_of_word)
#   ENDIF
# ENDIF
# END FUNCTION

def is_in_order(word):
    if len(word) == 1:
        return True
    else:
        first_char = word[0]
        #print(first_char)
        rest_of_word = word[1:len(word)]
        #print(rest_of_word)
        if first_char > rest_of_word:
            return False
        else:
            return is_in_order(rest_of_word)


print(is_in_order("fbdgs"))