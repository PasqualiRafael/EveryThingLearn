

def conversion(x):
    dollar = 5.64
    converter = dollar * x
    print(f'US$ {x:.2f} = R$ {converter:.2f}')


if __name__ == '__main__':
    user_value = int(input(f'Quantos dolares?\n' + 'US$: '))
    conversion(user_value)
    
    