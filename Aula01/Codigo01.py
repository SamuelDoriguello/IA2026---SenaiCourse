from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Aqui você define sua chave API
API =

agente = Agent(
    model = OpenAIChat(
        id = "GPT-5.4-nano",
        api_key = API,
    ),
    markdown = True,
)


pergunta = input("Digite uma pergunta: ")
agente.print_response(pergunta, stream = True)