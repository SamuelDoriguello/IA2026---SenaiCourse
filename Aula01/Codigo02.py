from agno.agent import Agent
from agno.models.openai import OpenAIChat


API = "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"


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

