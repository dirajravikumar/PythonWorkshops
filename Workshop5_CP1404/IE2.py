usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'darth6am3r','bob']

check_username = str(input("Enter your username: "))

if check_username in usernames:
    print("Access Granted!")
else:
    print("Access Denied!")