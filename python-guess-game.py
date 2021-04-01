import random
print('****Python Guess game****')
print('Rules are as follows: Thanks')
print('You have to guess any number from your choice')
print('You will have 10 chances if you match 4 times you win')
print('Lets start')
start,end=int(input('Enter starting of your choice: ')),int(input('Enter last number of your choice: '))
n=10
win=0
while n!=0:
    guess=int(input('Enter number between {} and {}:'.format(start,end)))
    comp_guess=random.randint(start,end)
    if guess==comp_guess:
        win+=1
    else:
        print('Not matched')
    print('You have matched {} times'.format(win))
    n-=1
if win>3:
    print('****Congratulations****\nYou have won with computer you have a sharp mind')
else:
    print('You lose..... try again')
