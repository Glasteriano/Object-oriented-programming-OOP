from context_manager_classes import Arquivo, abrir, File

with Arquivo('teste1.txt', 'w') as ideia:
    ideia.write('Algo\nAlgo 1\nAlgo 2')
# ______________________________________________

oi = File()

with oi.abrir('teste.txt', 'w') as oi:
    oi.write('Algo\nAlgo 1\nAlgo 2')
# ______________________________________________

with abrir('abc.txt', 'w') as file:
    file.write('Algo\nAlgo 1\nAlgo 2')
