def soma(e,b):
    return e+b
    
def soma_binaria(e, b):
    resultado = e + b
    print(f"\nBinário -> {bin(e)[2:]} + {bin(b)[2:]} = {bin(resultado)[2:]}")
    print(f"Decimal -> {e} + {b} = {resultado}")

e = int(input("Digite o 1º valor: "))
b = int(input("Digite o 2º valor: "))
print("\nA operação em números binários é:")
soma_binaria(e, b)
