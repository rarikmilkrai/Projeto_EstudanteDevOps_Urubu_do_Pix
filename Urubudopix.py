import random

# Definir a tabela de trading com valores de entrada e saída
tabela_trading = {
    200: 2000,
    250: 2500,
    300: 3000,
    350: 3500,
    400: 4000,
    500: 5000
}

# Função para gerar um token aleatório com letras, números e caracteres especiais
def gerar_token():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    token = ''.join(random.choice(caracteres) for _ in range(10))  # Laço de repetição (for) para criar um token de 10 caracteres
    return token

# Função para processar o pedido de PIX com base no valor de investimento
def fazer_pix(valor):
    if valor in tabela_trading:  # Uso de estrutura condicional (if) para verificar se o valor está na tabela
        retorno = tabela_trading[valor]  # Acesso a um valor em um dicionário
        token = gerar_token()  # Chama a função para gerar o token
        mensagem = f"PIX de R${valor} feito com sucesso! Token: {token}. Retorno: R${retorno}."
        return mensagem
    else:
        return "Valor de investimento não válido."

# Programa principal
print("Bem-vindo ao Urubu do PIX - Tabela Trading")
while True:
    try:
        valor_investimento = float(input("Digite o valor do investimento (em R$): "))  # Entrada de dados do usuário
        mensagem = fazer_pix(valor_investimento)  # Chama a função para processar o PIX
        print(mensagem)  # Saída de dados para o usuário
    except ValueError:
        print("Por favor, insira um valor válido.")  # Tratamento de erro se o usuário inserir um valor inválido
    continuar = input("Deseja fazer outro PIX? (S/N): ").strip().lower()  # Entrada de dados do usuário
    if continuar != 's':  # Uso de estrutura condicional (if) para verificar se o usuário deseja continuar
        break

print("Obrigado por usar o Urubu do PIX!")
