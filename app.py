course = input('Tell me a joke: ')

while len(course) == 20:
    print('Too many characters!')
    course = input('Tell me another joke: ')

if len(course) < 20:
    print('Funny')