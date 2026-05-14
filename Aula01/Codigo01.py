from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Aqui você define sua chave API
API = "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"


agente = Agent(
    model = OpenAIChat(
        id = "GPT-5.4-nano",
        api_key = API,
    ),
    markdown = True,
)


pergunta = input("Digite uma pergunta: ")
agente.print_response(pergunta, stream = True)