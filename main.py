codigo = int(0)
alcool = int(0)
gasolina = int(0)
diesel = int(0)
while codigo != 4:
    codigo = int(input())
    if codigo == 1:
        alcool = alcool + 1
    else:
        if codigo == 2:
            gasolina = gasolina + 1
        else:
            if codigo == 3:
                diesel = diesel + 1
print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))