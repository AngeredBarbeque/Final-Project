from InquirerPy import inquirer
from Crypto.Cipher import AES
import base64

def encrypt(password):
    key = b"The Eyes Of The Giant Bird's Leg"
    nonce = b'18420056'
    cipher = AES.new(key=key,mode=AES.MODE_CTR,nonce=nonce)
    cipher_text = base64.b64encode(cipher.encrypt(password)).decode()
    return cipher_text

def decrypt(password):
    key = b"The Eyes Of The Giant Bird's Leg"
    nonce = b'18420056'
    cipher = AES.new(key=key,mode=AES.MODE_CTR,nonce=nonce)
    plain = cipher.decrypt(base64.b64decode(password)).decode()
    return plain

def sign_in(users):
    if len(users) < 1:
        print('Please create an account before attempting to sign in.')
        return None
    usernames = []
    for i in users:
        usernames.append(i.get('Username'))
    username = inquirer.select(
        message='Select an account:',
        choices=usernames
    ).execute()
    #ADD PASSWORD CHECKING HERE
    for i in users:
        if username == i.get('Username'):
            print(f'Success! Signed in as {username}')
            return i
        
def create(users):
    username = inquirer.text(
        message='Enter a username:',
        validate=lambda result: len(username) < 1 or len(username) > 20,
        invalid_message='Username must be between 1 and 20 characters long.'
    ).execute()
    for i in users:
        if i.get('Username') == username:
            print('That username is taken.')
            return None
    password = inquirer.text(
        message='Enter a password:',
        validate=lambda result: len(username) < 8,
        invalid_message='Password must be longer than 8 characters'
    ).execute()
    password = encrypt(password)
    # ADD WRITNG TO FILE
    print({'Username':username,'Password':password})

def accounts_main():
    pass
    #FINISH HERE



#REPLACE WITH READ FILE FUNCTION
users = [{'Username':'User','Password':'Pass'},{'Username':'Tom','Password':'Bigglebutt'},{'Username':'Jonas','Password':'RQRT'},{'Username':'O','Password':'O is for Orangutan'}]
sign_in(users)