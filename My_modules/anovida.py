

def bpm_math(bpm):
    TotalMinutosAno = 525600
    TotalBpmAno = bpm * TotalMinutosAno
    total_bpm = 2700000000
    AnoVida = total_bpm // TotalBpmAno
    print(f'Sua espectativa de vida é: {AnoVida} anos.')
    return AnoVida


if __name__ == '__main__':
    x = int(input(f'Qual é seu Batimento por minuto?\n'))
    AnoVida = bpm_math(x)
    print(f'Sua espectativa de vida é: {AnoVida} anos.')
