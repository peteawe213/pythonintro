#guessing answer game (8/apr)
answer = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('(Number  )Guess: '))
    guess_count += 1
    if guess == answer:        #if guess is correct, need to terminate other guess q's
        print('You Win')
        break                  #breaks loop
else:
    print('Try again')

