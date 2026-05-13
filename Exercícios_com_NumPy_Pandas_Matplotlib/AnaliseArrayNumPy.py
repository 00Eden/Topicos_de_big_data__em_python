import numpy as np

temperaturas = np.array([22.5, 23.0, 19.5, 21.0, 25.2, 26.3, 24.5])

# 1.1 Média da semana
media = np.mean(temperaturas)

# 1.2 Maior e menor temperatura
maior = np.max(temperaturas)
menor = np.min(temperaturas)

# 1.3 Dias acima da média
acima_media = np.sum(temperaturas > media)

print(f"Média da semana: {media:.2f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Dias acima da média: {acima_media}")
