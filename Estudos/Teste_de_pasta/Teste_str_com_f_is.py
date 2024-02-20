print("""
    *************************** [J] ***************************
    IFCE Campos caucaia                          Turno: Noturno  
    Curso: Eng.Produção              Nome: Jefferson de Almeida
    ***********************************************************
""")
_var = str(input("Digite algo: "))

print("""
        A variável é número e/ou letra: {} 
        A variável é do alfabeto: {}
        A variável é da tabela ASCII: {}
        A variável é do tipo inteira: {}
        A variável começa com letra minúscula: {}
        A variável olha se !@#$%¨&* : {}
        A variável é do alfabeto: {}
        A variável é string e a 1º letra é alfabetica: {}
        A variável é string tabela é vazia: {}
        A variável é numérica: {}

""".format(
    _var.isalnum(),
    _var.isalpha(),
    _var.isascii(),
    _var.isdigit(),
    _var.islower(),
    _var.isalnum(),
    _var.isdecimal(),
    _var.isidentifier(),
    _var.isprintable(),
    _var.isnumeric()
    )
)
#print(_var*2)
# TODAS AS FUNÇÕES RETORNAM True(VERDADEIRO) OU False(FALSO)

# _var.isalnum -> testa se é uma letra ou um número ou ambos
# _var.isalpha -> testa se é uma letra do alfabeto
# _var.isascii -> testa se faz parte da tabela ASCII
# _var.isdigit -> testa se é uma variável inteira
# _var.islower -> testa se a primeira letra é minúscula
# _var.isalpha -> testa se é número e/ou letra, se for letra recebe Tre, se for @#$% recebe false
# _var.isdecimal -> testa se é uma variável inteira positiva maior ou igual a zero
# _var.isidentifier -> testa se é uma variável começa com letra do alfabeto
# _var.isprintable -> testa se é uma variável é uma tabela vazia
# _var.isnumeric -> testa se todos os dados da string são números, simbolos como - e + não funcionam
# _var.isdigit -> testa se é uma variável inteira
# _var.isdigit -> testa se é uma variável inteira
# _var.isdigit -> testa se é uma variável inteira












