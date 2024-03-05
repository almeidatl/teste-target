# Função para inverter uma string
def inverter_string(string):
    # Converter a string em uma lista de caracteres
    caracteres = list(string)
    
    # Iniciar os índices do começo e do fim da string
    inicio = 0
    fim = len(caracteres) - 1
    
    # Enquanto os índices não se cruzarem
    while inicio < fim:
        # Trocar os caracteres nas posições inicio e fim
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        
        # Avançar para o próximo caractere e retroceder para o anterior
        inicio += 1
        fim -= 1
    
    # Converter a lista de caracteres de volta para uma string
    string_invertida = ''.join(caracteres)
    
    # Retornar a string invertida
    return string_invertida

# Exemplo de entrada
entrada = input("Digite uma string para inverter: ")

# Chamar a função para inverter a string
string_invertida = inverter_string(entrada)

# Exibir a string invertida
print("String invertida:", string_invertida)
