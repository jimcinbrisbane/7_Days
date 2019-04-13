import random
wishes = random.randint(0,1)
religion = input('pls insert the avatar you believe in ')
wish = input('What do you wish? ')
if wishes == 0: print('Ur not faithful enough and '+ religion + ' Did not hear you')
else:
    print ('U got it all thx to' + religion)
