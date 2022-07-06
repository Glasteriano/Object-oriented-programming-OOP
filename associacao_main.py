from associacao_classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Jo Nesbø')
caneta = Caneta('Montblanc')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta  # Associando o escritor à caneta
escritor.ferramenta.escrever()  # Usando uma função da caneta através do escritor
escritor.ferramenta.escrevendo(escritor.nome)  # Usando métodos da classe Caneta através do escritor

escritor.ferramenta = maquina  # Associando o escritor à caneta
escritor.ferramenta.escrever()  # Usando uma função da máquina através do escritor
escritor.ferramenta.escrevendo(escritor.nome)  # Usando métodos da classe Maquina através do escritor
