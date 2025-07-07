import re
import statistics

tempos = []

with open("log.txt", "r") as arquivo:
    for linha in arquivo:
        match = re.search(r"Tempo de execução:\s*([\d.]+)s", linha)
        if match:
            tempo = float(match.group(1))
            tempos.append(tempo)

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    print(f"Média: {media:.2f}s")
    print(f"Desvio padrão: {desvio:.2f}s")
else:
    print("Nenhum tempo encontrado no arquivo.")
