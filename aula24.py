"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carroa
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_2 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

calculo_range_1 = local_carro >= (LOCAL_2 - RADAR_RANGE)
calculo_range_2 = local_carro <= (LOCAL_2 + RADAR_RANGE)

velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = calculo_range_1 and calculo_range_2

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_do_carro_passou_radar_1

if velocidade > RADAR_1:
    print('o carro foi multado')

if carro_passou_radar_1:
    print('carro passou radar 1')

if carro_multado_radar_1:
    print(' o carro foi miultado ')