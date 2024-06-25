dibujo_ahorcado = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''', 
    '''
       +---+
       |   |
       🫅   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       🫅   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       🫅   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       🫅   |
      /|\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       🫅   |
      /|\  |
      /    |
           |
    =========
    ''',
]

palabra = list('calavera')

palabra_oculta =['_']*len(palabra)

intentos = 6

lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')

letras_descartadas = []

def mostrar_estado():
    print(f'Intentos restantes: {intentos}')
    print(f'Letras descartadas: {", ".join(letras_descartadas)}\n')
    print(f'Palabra: {" ".join(palabra_oculta)}\n')
    print(dibujo_ahorcado[6 - intentos])
    
def letra_valida(letra):
    if len(letra) != 1 :
        print('Has puesto más de una letra, inténtalo de nuevo.')
        return False
    elif letra not in lista_abecedario:
        print('No has introducido una letra del abecedario')
        return False
    elif letra in palabra_oculta:
        print('La letra que has introducido ya la has acertado, inténtalo de nuevo.')
        return False
    elif letra in letras_descartadas:
        print('Esa letra ya la habías dicho, inténtalo de nuevo.')
        return False
    else:
        return True
      
def gestion_letra(letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            palabra[i] = '_'
            
print('JUEGO DEL AHORCADO\n')
print(f'Tienes {intentos} intentos. ¡Buena suerte!')

while intentos > 0 and '_' in palabra_oculta:
    mostrar_estado()
    print('-'*50)
    letra = input('INTRODUCE LETRA: ').lower()

    while not letra_valida(letra):
        letra = input('INTRODUCE OTRA LETRA: ').lower()

    if letra in palabra:
        gestion_letra(letra)
        print('-'*50)
        print('¡Has acertado la letra! Sigue así.')
    else:
        print('-'*50)
        print('¡Has fallado la letra!')
        letras_descartadas.append(letra)
        intentos -= 1

if '_' not in palabra_oculta:
    print('\n\nGANASTE')
else:
    print(f'\nPERDISTE'
        '''\n
       +---+
       |   |
      💀   |
      /|\  |
      / \  |
           |
    =========
    ''')