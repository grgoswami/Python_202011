

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = 'NewYorkCity$@#'

if len(password) < 6:
    print('Your password is too short; it should have at least 6 characters')
else:
    if len(password) > 20:
        print('Your password is too long; it should have at most 20 characters')
    else:
        if ('$' not in password) and ('#' not in password) and ('@' not in password):
            print('Your password needs to have at least one of the following: $, #, @')
        else:
            flag = False
            for it in range(10):
                if str(it) in password:
                    flag = True
                    break
            if flag is False:
                print('Your passsword should contain at least one number')
            else:
                pass
        