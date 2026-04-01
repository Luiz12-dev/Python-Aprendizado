stack_bruta = ["Java", "Python", "Java", "Angular", "Python", "Python"]


frequencia = {}

for tec in stack_bruta:
    if tec not in frequencia:
        frequencia[tec] = tec.count(stack_bruta)
    else:
        frequencia.values() + 1
print(frequencia)
