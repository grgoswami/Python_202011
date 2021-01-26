
# Here minimum_length is a keyword argument
# Here password is a positional argument
def password_checker(password, minimum_length=6, maximum_length=20):
    if len(password) < minimum_length:
        print('Your password is too short; it should have at least {0} characters'.format(minimum_length))
    else:
        if len(password) > maximum_length:
            print('Your password is too long; it should have at most {0} characters'.format(maximum_length))
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

password_checker('NewYorkCity$@#')
password_checker('NewYorkCity$@#1')
password_checker('NewYorkCity')

password_checker('Ne$#1', minimum_length=5)
password_checker('Ne$#1')




        