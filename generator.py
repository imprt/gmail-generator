import random
chars='abcdefghijklmnopqrstuvwxyz1234567890'
loginen=random.randint(4,15)
login=''
for i in range (loginen):
    pos=random.randint(0,len(chars)-1)
    login=login+chars[pos]
if login [0].isnumeric():
    pos=random.randint(0,len(chars)-10)
    login=chars[pos]+login
servers=['@gmail', '@yahoo', '@redmail', '@hotmail']
servpos=random.randint(0,len(servers)-1)
email=login+servers[servpos]
tlds=['.com']
tldpos=random.randint(0,len(tlds)-1)
email=email+tlds[tldpos]
print(email)