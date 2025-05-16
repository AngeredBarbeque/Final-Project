try:
    from InquirerPy import inquirer
    from InquirerPy.validator import EmptyInputValidator as EIV
    from Crypto.Cipher import AES
except:
    pass
import base64
import os

#Encrypts a password and returns the encrypted text.
def encrypt(password):
    key = b"The Eyes Of The Giant Bird's Leg"
    nonce = b'18420056'
    cipher = AES.new(key=key,mode=AES.MODE_CTR,nonce=nonce)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode())).decode()
    return cipher_text

#Decrypts an encrypted password and returns the decrypted text.
def decrypt(password):
    key = b"The Eyes Of The Giant Bird's Leg"
    nonce = b'18420056'
    cipher = AES.new(key=key,mode=AES.MODE_CTR,nonce=nonce)
    plain = cipher.decrypt(base64.b64decode(password)).decode()
    return plain

#Returns a user profile after making the user select a profile.
def sign_in(users):
    if len(users) < 1:
        print('Please create an account before attempting to sign in.')
        return None
    usernames = []
    for i in users:
        usernames.append(i.get('name'))
    username = inquirer.select(
        message='Select an account:',
        choices=usernames
    ).execute()
    password = inquirer.text(
        message='Enter your password',
        validate=EIV,
        invalid_message='Password cannot be empty.'
    ).execute()
    for i in users:
        if username == i.get('name') and encrypt(password) == i.get('password'):
            print(f'Success! Signed in as {username}.')
            return users[users.index(i)]
    print('Incorrect Password.')
    return None
        
#Creates an account
def create(users):
    username = inquirer.text(
        message='Enter a username:',
        validate=lambda username: len(username.split()) > 1 or len(username.split()) < 20,
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
    users.append({'name':username,'password':password,'unlocked':0,'scores':[[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0],[100000,0]],'preferences':20})
    print("Your account was created successfully.")
    return users

#Allows the user to create an account or sign in
def accounts_main(users, user_info):
    while True:
        os.system('cls')
        if not user_info:
            choice = inquirer.select(
                message='What would you like to do?',
                choices=['Sign In','Create Account','Exit to main menu']
            ).execute()

            match choice:
                case 'Sign In':
                    user_info = sign_in(users)
                    input("Done reading?: ")
                case 'Create Account':
                    users = create(users)
                    input("Done reading?: ")
                case 'Exit to main menu':
                    return user_info, users
        else:
            choice = inquirer.select(
                message='What would you like to do?',
                choices=['Sign Out','Options','Delete Account','Exit to main menu']
            ).execute()

            match choice:
                case 'Sign Out':
                    user_info = None
                    print("Successfully logged out.")
                    input("Done reading?: ")
                case 'Options':
                    while True:
                        os.system("cls")
                        action = inquirer.select(
                            message='Options',
                            choices=['Screen Size', 'Exit']
                        ).execute()

                        match action:
                            case "Screen Size":
                                screen_size = int(inquirer.number(
                                    message="Select screen size:",
                                    min_allowed=10,
                                    max_allowed=30,
                                    validate=EIV(),
                                ).execute())
                                user_info["preferences"] = screen_size
                            case "Exit":
                                break

                case 'Delete Account':
                    del users[users.index(user_info)]
                    user_info = None
                    print("Successfully deleted account.")
                    input("Done reading?: ")

                case 'Exit to main menu':

                    return user_info, users