import random
import time

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
servers = ['@gmail']
tlds = ['.com']

while True:
    login_len = random.randint(4, 15)
    login = ''.join(random.choice(chars) for _ in range(login_len))

    if login[0].isnumeric():
        login = random.choice(chars[:-10]) + login

    servpos = random.randint(0, len(servers) - 1)
    tldpos = random.randint(0, len(tlds) - 1)

    email = login + servers[servpos] + tlds[tldpos]
    print('Gmail -->', email)

    time.sleep(1)

