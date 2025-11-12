#Colocar título e descrever o jogo.
print("JOGO DE PERGUNTAS")

print("O jogo será trabalhado na forma de utilizar dados externos, para desenvolver respostas e novas perguntas, utilizando a idéia de INPUT")
#Pensar em um tema...
nome = input("Qual é seu nome?")
print("Oi" ,nome)

pontos = 0;

#pergunta1
matemático = input("Qual foi o matemático que desenvolveu a seguinte fórmula, a² = b² + c²")
if matemático == "Pitágoras" or matemático == "pitagoras":
     print("Parabéns", nome,",você acertou.🤓")
     pontos += 1
else: 
     print("Que pena", nome, "você errou 🤔")
