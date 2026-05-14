from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb


API = ""

agenteMemo = Agent(
    model = OpenAIChat(
        id = "gpt-4.1",
        api_key = API,
        instructions= "Você é um jogador de basketball que joga na NBA no time Lakers"
                      "Você sempre responde como se estivesse em uma entrevista pós jogo"
                      "No final do jogo você estará cansado, descreva entre áspas gestos e comportamentos como '(secando suor) e etc' nas pausas entre as frases"
                      "Seja sempre otimista ao estilo de um jogador convincente"
    ),
    db = SqliteDb(db_file = "agent.db"),
    num_history_runs = 5,
    add_history_to_context = True,
    markdown = True
)

while True:
    pergunta = input("\nDigite sua pergunta ou 'shutdown' para sair: ")
    if pergunta.lower() == "shutdown":
        break
    agenteMemo.print_response(pergunta, stream = True)