import pyautogui as pt
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from pathlib import Path


API =


def tela() -> str:
    pt.hotkey('win', 'd')
    pt.sleep(1)
    pt.press('win')
    pt.sleep(1)
    pt.write('fer')
    pt.sleep(1)
    pt.press('enter')
    pt.sleep(2)
    pt.hotkey('ctrl', 'n')
    pt.sleep(3)
    pt.hotkey('ctrl', 's')
    pt.sleep(3)
    pt.write(r"C:\Users\FIC\Documents\IA2026\Aula02\tela.png")
    pt.sleep(1)
    pt.press('enter')
    pt.sleep(1)
    pt.press('s')
    pt.sleep(1)
    pt.press('enter')
    pt.sleep(1)
    pt.hotkey('alt', 'tab')


agenteCopiarTela = Agent(
    model = OpenAIChat(
        id = "gpt-4o",
        api_key = API,
        instructions =  """
                        Você é um agente que tira print da tela do computador e fala para o usuário
                        os ícone que tem na tela, descreve os nomes dos arquivos e organiza tudo em formatos de tablea.
                        REGRA:
                        - Somente apresentar a tabela na saída de dados.
                        - Utilizar sempre a tool criada para tirar o print da tela
                        """
    ),
    db = SqliteDb(db_file = "print.db"),
    num_history_runs = 5,
    add_history_to_context = True,
    markdown = True,
    tools = tela(),
)


#Caminho da imagem local
imagem_caminho = Path('tela.png')
imagem_bytes = imagem_caminho.read_bytes()
agenteCopiarTela.print_response(
        """ Quero que você analise os aplicativos que estão na imagem e faça uma descrição detalhada deles e os separe por categorias.
                """,
    images = [Image(content = imagem_bytes)]
)
