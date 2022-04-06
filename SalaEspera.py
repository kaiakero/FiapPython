nome=input("Digite seu nome")
idade=int(input("Digite a idade "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade >=65:
    print("o paciente " + nome + "POSSUI atendimento prioriário!" )
elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + " Deve ser direionado para sala de espera reservada")
else:
    print("O paciente " + nome + " NÂO possui prioridade e pode aguardar na sala comum")