import json

class Gerenciar_Save:
    """
    Classe utilitária para manipulação de arquivos de save em formato JSON.
    Permite salvar e recuperar o estado completo do jogador entre sessões de jogo.
    """
    def __init__(self, nome_arquivo='save.json'):
        self.nome_arquivo = nome_arquivo

    def salvar(self, jogador):
        """Converte o estado atual do objeto Jogador em um formato JSON e salva no disco."""
        dados = {}
        dados['classe'] = jogador.classe
        dados['vida'] = jogador.vida
        dados['mana'] = jogador.mana
        dados['defesa'] = jogador.defesa
        dados["progresso_historia"] = jogador.progresso_historia
        
        # Serialização do inventário
        dados['inventario'] = []
        for item in jogador.inventario:
            dados_do_item = {}
            dados_do_item['nome'] = item.nome
            categoria_de_item = item.categoria

            if categoria_de_item == 'arma':
                dados_do_item['tipo'] = 'arma'
                dados_do_item['dano'] = item.dano
            elif categoria_de_item == 'pocao':
                dados_do_item['tipo'] = 'pocao'
                dados_do_item['valor'] = item.valor_recuperacao
                dados_do_item['subtipo'] = item.tipo

            dados['inventario'].append(dados_do_item)

        # Serialização da arma atualmente equipada
        arma_na_mao = jogador.arma_escolhida
        if arma_na_mao != None:
            dados['arma_equipada'] = {
                "nome": jogador.arma_escolhida.nome,
                "dano": jogador.arma_escolhida.dano
            }
        else:
            dados['arma_equipada'] = None

        # Escrita física no arquivo de saída
        texto_json = json.dumps(dados, indent=4)
        arquivo_aberto = open(self.nome_arquivo, 'w')
        arquivo_aberto.write(texto_json)
        arquivo_aberto.close()

        print('Jogo salvo com sucesso!')

    def carregar(self):
        """Lê o arquivo de save e retorna os dados convertidos de JSON para um dicionário Python."""
        try:
            arquivo_aberto = open(self.nome_arquivo, 'r')
            conteudo_do_texto = arquivo_aberto.read()
            arquivo_aberto.close()

            dados_convertidos = json.loads(conteudo_do_texto)
            return dados_convertidos
        except FileNotFoundError:
            # Caso o arquivo não exista, retorna None para indicar que é um novo jogo
            return None
        except Exception as e:
            # Captura erros inesperados na leitura/parsing do JSON
            print(f"Erro ao carregar o save: {e}")
            return None






