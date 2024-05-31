import psutil

bateria = psutil.sensors_battery()

percentual_bateria = str(bateria.percent)

print(f'este notebook está com {percentual_bateria}% de bateria!')

plugado = bateria.power_plugged

if plugado:
    print('o notebook está conectado na tomada!')
else:
    print('o notebook está desconectado da tomada!')