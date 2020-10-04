
import colors


def ini(title):      
      print(f'')
      print('{}'.format(colors.cores['bw']) + 
      ('-=-' * 12) + '{}'.format(colors.cores['close']))
      print('{:-^36}'.format(title))
      print('{}'.format(colors.cores['bw']) +
      ('-=-' * 12) + '{}'.format(colors.cores['close']))
      print(f'')


def close():      
      print(f'')
      print('{}'.format(colors.cores['bw']) +
      ('-=-' * 12) + '{}'.format(colors.cores['close']))
      input('{}Pressione qualquer tecla para fechar!{}'.format(
      colors.cores['green'], colors.cores['close']))

if __name__ == '__main__':
      ini(' Funciona ')
      close()