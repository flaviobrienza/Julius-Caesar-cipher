import string

alphabet = ' ' + string.ascii_lowercase
positions = {' ':0,
'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26}

positions2=dict()
for k,v in positions.items():
    positions2[v]=k

message = 'hi my name is flavio'
encoded_message = ''

for e in message:
    e = positions[e]
    e = e + 1
    e = positions2[e]
    encoded_message += e


def encoding(message, key):
    encoded_message = '' 
    for e in message:
        e = positions[e] 
        e = (e + key) % 27 
        e = positions2[e]
        encoded_message += e 
    return encoded_message

def decoding(message, key):
    decoded_message = ''
    for x in message:
        x = positions[x]
        x = (x - key) % 27
        x = positions2[x]
        decoded_message += x
    return decoded_message 

print(encoding(message, 5))
print(decoding(encoding(message,5), 5 ))
