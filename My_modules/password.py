from getpass import getpass
"""
getpass make password became invisible
"""
username = input('Username: ')
password = getpass()

print(username, password)