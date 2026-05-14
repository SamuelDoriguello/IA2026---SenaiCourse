from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import sqlite
from agno.tools.hackernews import HackerNewsTools

from Aula01.Codigo03 import API

API = "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"


agentHackerNews = Agent(
    model = OpenAIChat(
        id = "gpt-3.5-turbo",
        api_key = API,
        instructions =  """
                        Você é um assistente útil que responde perguntas para os alunos
                        do cursto de Inteligência Artificial Generativa Aplicado a programação do SENAI Americana,
                        sempre sendo objetivo e claro. Você estará lidando com um público na faixa etária de 10 anos.
                        """
    ),
    db = SqliteDb(db_file = "senai.db"),
    add_history_to_context = True,
    num_history_runs = 2,
    tools = [HackerNewsTools()],
    markdown = True,
)

while True:
    pergunta = input("\nDigite sua pergunta ou 'poweroff' para sair: ")
    if pergunta == "poweroff":
        break
    agentHackerNews.print(pergunta)