equipamento = []
valor = []
serie = []
setor = []
resposta = 'S'

while resposta == 'S':
    equipamento.append(input('Equipamento:  '))
    valor.append(float(input('Valor estimado do Equipamento:  ')))
    serie.append(int(input('Informe o numero de serie do equipamento:  ')))
    setor.append(input('Informe o setor do equipameto:  '))
    resposta = input('digite "sim" para adicionar um elemento')

    for indice in range(0,len(equipamento)):
        print ('Equipamento', (indice+1))
        print (f'nome......:  {equipamento[indice]}')
        print (f'valor......:  {valor[indice]}')
        print (f'serial......:  {serie[indice]}')
        print (f'setor......:  {setor[indice]}')


