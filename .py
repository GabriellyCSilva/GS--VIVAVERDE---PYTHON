# Luiza Saraçol Ribeiro - RM560200
# Gabrielly Cândido Camargo da Silva - RM560916
# Estefany Caetano de Jesus - RM560181

# Solicitamos ao usuário as informações básicas para configurar a simulação.
capacidade_geracao_solar = float(input("Digite a capacidade de geração de energia solar (kWh/dia): "))
capacidade_geracao_eolica = float(input("Digite a capacidade de geração de energia eólica (kWh/dia): "))
num_casas = int(input("Digite o número de casas na comunidade: "))
consumo_por_casa = float(input("Digite o consumo médio de energia por casa (kWh/dia): "))
dias_simulacao = int(input("Digite o número de dias para simulação: "))

# Coletamos dados financeiros e históricos para deixar a análise mais completa.
custo_kwh = float(input("Digite o custo médio do kWh de energia elétrica na sua região (em R$): "))
conta_agua_mensal = float(input("Digite o valor médio da sua conta de água mensal (em R$): "))
consumo_mensal_anterior = float(input("Digite o consumo médio de energia (kWh/mês) antes de usar energia renovável: "))

# Função para calcular o consumo total da comunidade.
def calcular_consumo_total(num_casas, consumo_por_casa, dias):
    """Calcula o consumo total de energia baseado no número de casas e dias simulados."""
    return num_casas * consumo_por_casa * dias

# Função para calcular a geração total de energia renovável.
def calcular_geracao_total(capacidade_solar, capacidade_eolica, dias):
    """Calcula a geração total de energia com base na capacidade solar e eólica disponíveis."""
    return (capacidade_solar + capacidade_eolica) * dias

# Função para calcular o valor da conta de luz.
def calcular_valor_conta(consumo_total, custo_kwh):
    """Calcula o valor estimado da conta de luz para o consumo informado."""
    return consumo_total * custo_kwh

# Calculamos o consumo total da comunidade e a geração de energia renovável.
consumo_total = calcular_consumo_total(num_casas, consumo_por_casa, dias_simulacao)
geracao_total = calcular_geracao_total(capacidade_geracao_solar, capacidade_geracao_eolica, dias_simulacao)
valor_conta_luz = calcular_valor_conta(consumo_total, custo_kwh)

# Apresentamos os resultados para o usuário.
print("\n Resultados da Simulação ")
print(f"Consumo total da comunidade: {consumo_total} kWh")
print(f"Geração total de energia renovável: {geracao_total} kWh")
print(f"Valor estimado da conta de luz: R$ {valor_conta_luz:.2f}")

# Analisamos se a comunidade é autossuficiente em energia ou não.
if geracao_total >= consumo_total:
    excedente = geracao_total - consumo_total
    print(f"A comunidade é autossuficiente em energia! Excedente de {excedente} kWh que pode ser armazenado ou compartilhado.")
else:
    deficit = consumo_total - geracao_total
    print(f"A comunidade não é autossuficiente em energia. Déficit de {deficit} kWh. Considere aumentar a geração ou reduzir o consumo.")

# Calculamos quanto a comunidade economizou em relação ao consumo anterior.
economia = (consumo_mensal_anterior - consumo_total) * custo_kwh
print("\n Comparação com Consumo Anterior ")
print(f"Consumo médio mensal antes da energia renovável: {consumo_mensal_anterior} kWh")
print(f"Economia estimada na conta de luz: R$ {economia:.2f}")
print(f"Conta de água média mensal informada: R$ {conta_agua_mensal:.2f}")

# Adicionamos dicas práticas para ajudar na economia de energia.
print("\n Dicas de Economia de Energia")
if consumo_por_casa > 10:
    print("1. Reduza o uso de aparelhos que consomem muita energia, como ar-condicionado e aquecedores.")
    print("2. Prefira lâmpadas de LED em vez de incandescentes, pois consomem menos energia.")
    print("3. Aproveite ao máximo a luz natural durante o dia, reduzindo o uso de iluminação artificial.")
    print("4. Desligue aparelhos eletrônicos quando não estiverem em uso.")
else:
    print("Parabéns! O consumo médio por casa está em um nível sustentável.")
    print("Continue usando a energia de forma consciente para manter esse ótimo desempenho!")
