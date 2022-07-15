from criando_excecoes_classes import ConteudoDentro, Vazio

teste1 = ConteudoDentro()
teste1.testar()  # Se não tiver argumento aparece a mensagem programada

teste2 = Vazio()
teste2.executando_nada()  # Mostrando o êrro levantado na classe
teste2.nada()  # Executando-o directamente, será mostrada a quebra do código
