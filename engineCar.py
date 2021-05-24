command = " "
started = False
stopped = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('car already ready')
        else:
            started = True
            print('car ready')
    elif command == 'stop':
        if not started:
            print('car alreaady stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print('''start - to start car
stop - to stop car
quit - quit
        ''')
    elif command == 'quit':
        break
    else:
        print("I don't understand")


'''
car = str(input('> '))              #my code for exercise 1:32:00
if car == 'help':
    print('start - to start car')
    print('stop - to stop car')
    print('quit - to quit')
else:
    print("I don't understand")

to_do = str(input('> '))
if to_do == 'start':
    print('car started')

    if to_do == 'stop':
        print('car stopped')
        if to_do == 'quit':
            print('done')

else:
    print("I don't understand")
'''








