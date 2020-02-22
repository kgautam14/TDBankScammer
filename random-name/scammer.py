import os
import requests
import random
import string
import json

def main():
    chars = string.ascii_letters + string.digits + '(!@#$%^&*())'
    random.seed = (os.urandom(1024))

    # This is the url where your username and password is being redirected.
    url = 'https://authentication.td.com/waw/idp/authn/v1/authenticate/basic?lang=en_CA'

    input_file = open('names.json', 'r', encoding='utf-8')
    names = json.load(input_file)

    input_mid = open('middle-names.json', 'r', encoding='utf-8')
    middle_names = json.load(input_mid)

    for name in names:

        name_extra = ''.join(random.choice(string.digits))
        name = name + name_extra + middle_names[random.randint(1, 3896)] + '@gmail.com'

        username = name
        password = ''.join(random.choice(chars) for i in range(8))

        requests.post(url, allow_redirects=False, data={
            'loginId': username,
            'password': password
        })

        print('Sending username %s and password %s' % (username, password))


if __name__ == '__main__':
    main()
