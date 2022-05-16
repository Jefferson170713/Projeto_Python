print("""
    *************************** [J] ***************************
    IFCE Campos caucaia                          Turno: Noturno  
    Curso: Eng.Produção              Nome: Jefferson de Almeida
    ***********************************************************
""")
_id = int(input("Digite uma idade: "))

if _id <= 12:
    print("Criança")
elif _id < 18:
    print("Adolescente")
elif _id < 60:
    print("Adulto")
else:
    print("Idoso")

# Testando o if, podemos perceber que temos a estrutura if de apenas uma condição.
# Temos a estrutura if-else, onde testa duas condições, se não atender a primeira, vai para o else
# Temos a última sequência, if-elif.. ... ..elif-else, uma estrutura com várias condições
#   implementada com uma última validação caso todas as intermediárias falhem, que é o else.



