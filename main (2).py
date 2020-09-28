# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
class Regex():
    def __init__(self, string):
        self.string = string

    def varify_email_address(self):
        email = string.split('<')
        if re.match('^[a-z][a-z0-9-._]+@[a-z]+[.][a-z]{1,3}[>]$', email[1],re.I):
            print(string)
        else:
            pass

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        string = input()
        my_object = Regex(string)
        my_object.varify_email_address()
