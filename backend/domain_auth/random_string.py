
import secrets
import string

# initializing size of string
N = 40


def get_string():

    return ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                   for i in range(N))

# print result
