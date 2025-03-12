# conhecendo a base
import csv
reader = csv.reader(open('steam_games.csv'))
dados = []
for linha in reader:
    dados.append(linha)

# coluna do preco
dados[1][6]

# diminuindo o banco para facilitar a analise exploratoria
menos_dados = dados[:100]

# encontrando os gratuitos
dados = menos_dados
gratuitos = []
primeira = True
for dado in dados:
    if primeira:
        primeira = False
        continue
    preco = float(dado[6])
    if preco == 0:
        gratuitos.append(dado)
print(len(dados))
print(len(gratuitos))


# trabalhando com o banco completo
import csv
reader = csv.reader(open('steam_games.csv'))
dados = []
for linha in reader:
    dados.append(linha)
gratuitos = []
primeira = True
for dado in dados:
    if primeira:
        primeira = False
        continue
    preco = float(dado[6])
    if preco == 0:
        gratuitos.append(dado)

# respondendo à primeira pergunta
# Qual o percentual de jogos gratuitos e pagos na plataforma? 
porcentagem_gratuitos = len(gratuitos) / len(dados)
porcentagem_pagos = 1 - porcentagem_gratuitos
print(f'Temos {porcentagem_gratuitos:.2%} de jogos gratuitos e {porcentagem_pagos:.2%} de jogos pagos')


# respondendo à segunda pergunta
# Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados

anos_de_lancamentos = []

primeira = True
for dado in dados:
    if primeira:
        primeira = False
        continue
    ano_lancamento = int(dado[2][-4:])
    anos_de_lancamentos.append(ano_lancamento)

anos_unicos = set(anos_de_lancamentos)

anos_e_lancamentos = []
for ano in anos_unicos:
    anos_e_lancamentos.append([ano, anos_de_lancamentos.count(ano)])

ano_mais_jogos = max(anos_e_lancamentos, key=lambda x: x[1])

print(f'Ano com mais jogos: {ano_mais_jogos[0]} com {ano_mais_jogos[1]} jogos')



class DadosJogos:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados = []
        self.load_data()

    def load_data(self):
        """Carrega os dados do CSV ignorando a primeira linha (cabeçalho)"""
        with open(self.nome_arquivo, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.data = list(reader)[1:]  # Remove cabeçalho
            
    def get_data(self):
        """Retorna os dados carregados."""
        return self.data

class AnalizadorJogos:
    """Classe responsável por analisar os dados e responder às perguntas"""
    
    def __init__(self, dados_jogos):
        self.dados = dados_jogos
    
    def porcentagem_jogos_gratuitos(self):
        """Retorna a porcentagem de jogos gratuitos"""
        total_jogos = len(self.dados)
        total_jogos_gratuitos = 0
        
        for dado in self.dados:
            preco = float(dado[6])
            if preco == 0:
                total_jogos_gratuitos += 1
        
        porcentagem_gratuitos = total_jogos_gratuitos / total_jogos
        porcentagem_pagos = 1 - porcentagem_gratuitos
        
                
        return porcentagem_gratuitos, porcentagem_pagos
    
    def anos_mais_jogos(self):
        """Retorna o ano com o maior número de novos jogos"""
        anos_de_lancamentos = []
        
        primeira = True
        for dado in self.dados:
            if primeira:
                primeira = False
                continue
            ano_lancamento = int(dado[2][-4:])
            anos_de_lancamentos.append(ano_lancamento)
        
        anos_e_lancamentos = []
        for ano in anos_unicos:
            anos_e_lancamentos.append([ano, anos_de_lancamentos.count(ano)])

        ano_mais_jogos = max(anos_e_lancamentos, key=lambda x: x[1])
        
        return ano_mais_jogos



# ================================
# EXECUÇÃO PRINCIPAL
# ================================

# Carrega os dados
dados_jogos = DadosJogos("steam_games.csv")

# Cria o analisador com os dados carregados, usando o método get.data
analizador = AnalizadorJogos(dados_jogos.get_data())

# Responde às perguntas
porcentagens = analizador.porcentagem_jogos_gratuitos()
ano_mais_jogos = analizador.anos_mais_jogos()

# Exibir resultados
print(f'Temos {porcentagens[0]:.2%} de jogos gratuitos e {porcentagens[1]:.2%} de jogos pagos')
print(f'Ano com mais jogos foi {ano_mais_jogos[0]}, com {ano_mais_jogos[1]} jogos')

