# Challenge #14
# Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".
# If the email is not valid the script should display why it's not valid.
# We consider a valid email address if:
# it has at least 6 characters but no more than 16.
# it contains both . and @
# it does not contain any of the following characters:'[]{}()$*'
    
not_wanted = '[]{}()$*'
wanted = '.@'
while True:
    e_mail = input('input your mail:')
    if 6 > len(e_mail) or 16 < len(e_mail):
        print("invalid email number of characters should be btw 6 and 16")
    elif not set(not_wanted).isdisjoint(set(e_mail)):
        print("invalid, cannot contain any of the symbols '[]{}()$*' ")
    elif set(wanted).intersection(set(e_mail)) != set('.@'):
        print("invalid email has to contain '.' and '@'")
    else:
        print('valid email')
        break

