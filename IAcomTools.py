from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.tools.hackernews import HackerNewsTools


API =

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
    agentHackerNews.print_response(pergunta)