from agno.agent import Agent
from agno.models.openai import OpenAIChat


API =

agenteDeIA = Agent (
    model = OpenAIChat(
        id = "gpt-4.1",
        api_key = API,
        instructions = "Você é um pirata chamado Davy Jones"
                       "Você sempre responde como um marujo dos sete mares"
                       "Sempre começando com a palavra Glup, e dê a sua resposta"
                       "Você gosta de contar histórias aleatórias sobre suas aventuras nos sete mares"
    ),
    markdown = True,
)


while True:
    print("")
    pergunta = input("Digite sua pergunta ou 'shutdown' para sair: ")
    if pergunta.lower() == "shutdown":
        break
    agenteDeIA.print_response(pergunta, stream=True)

