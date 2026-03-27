limite = 3

usuario_ativo = True

for tentativa in range(limite):
    if usuario_ativo == True:
        print(f"Tentativa {tentativa} liberada !")
    else:
        print("Usuário Bloqueado")
print("Processo finalizado !")


