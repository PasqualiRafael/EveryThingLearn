import pasqualiFinal
from colors import cores

pasqualiFinal.ini('challenge hackerrank')

N = int(input(f'Choose one number\n'))


if N % 2 == 1:
    print(f'{cores["red"]}Weird{cores["close"]}')
else:
    if N in range(2, 6):
        print(f'Not Weird')
    elif N in range(6, 21):
        print(f'Weird')
    else:
        print(f'Not Weird')


pasqualiFinal.close()
