import json # Biblioteca para lidar com arquivos JSON (texto organizado)

class GerenciadorSave:
    # O __init__ prepara a classe com o nome do arquivo de save.
    def __init__(self, nome_arquivo="save_jogo.json"):
        self.nome_arquivo = nome_arquivo

    # Esta função pega os dados do jogador e escreve no arquivo.
    def salvar(self, jogador):
        # --- PASSO 1: INICIAR O DICIONÁRIO ---
        # O dicionário 'dados' começa vazio: {}
        dados = {} 
        
        # Adicionamos a classe: {"classe": "Mago"}
        dados["classe"] = jogador.classe 
        # Adicionamos a vida ao que já existe: {"classe": "Mago", "vida": 80}
        dados["vida"] = jogador.vida     
        # Adicionamos a mana: {"classe": "Mago", "vida": 80, "mana": 150}
        dados["mana"] = jogador.mana     
        # Adicionamos a defesa: {..., "defesa": 5}
        dados["defesa"] = jogador.defesa 
        
        # Criamos uma lista vazia para guardar os itens: {"inventario": [], ...}
        dados["inventario"] = []

        # --- PASSO 2: MONTAR A LISTA DE ITENS ---
        for item in jogador.inventario:
            # Para cada item, criamos um dicionário temporário com seus detalhes
            dados_do_item = {}
            dados_do_item["nome"] = item.nome # Ex: {"nome": "Espada"}
            
            if item.categoria == "arma":
                dados_do_item["tipo"] = "arma"
                dados_do_item["dano"] = item.dano # Ex: {"nome": "Espada", "tipo": "arma", "dano": 15}
            elif item.categoria == "pocao":
                dados_do_item["tipo"] = "pocao"
                dados_do_item["valor"] = item.valor_recuperacao
                dados_do_item["subtipo"] = item.tipo # Ex: {"nome": "Poção", "tipo": "pocao", "valor": 20, "subtipo": "vida"}
            
            # Colocamos esse dicionário do item dentro da lista de inventário em 'dados'
            dados["inventario"].append(dados_do_item)

        # --- PASSO 3: DEFINIR ARMA EQUIPADA ---
        if jogador.arma_escolhida != None:
            # Criamos um dicionário para a arma e guardamos na chave "arma_equipada"
            dados["arma_equipada"] = {
                "nome": jogador.arma_escolhida.nome,
                "dano": jogador.arma_escolhida.dano
            }
        else:
            # Se não houver arma, a chave recebe o valor nulo (None)
            dados["arma_equipada"] = None

        """
        EXEMPLO VISUAL DO DICIONÁRIO 'DADOS' APÓS ESSAS LINHAS:
        {
            "classe": "Guerreiro",
            "vida": 100,
            "mana": 20,
            "defesa": 10,
            "inventario": [
                {"nome": "Espada de Ferro", "tipo": "arma", "dano": 15},
                {"nome": "Poção de Cura", "tipo": "pocao", "valor": 30, "subtipo": "vida"}
            ],
            "arma_equipada": {}
        }
        """

        # --- PASSO 4: TRANSFORMAR EM TEXTO ---
        # O computador não salva o 'dicionário' direto, ele precisa transformar em TEXTO.
        # O json.dumps faz essa mágica. indent=4 deixa o texto organizado para humanos lerem.
        texto_organizado = json.dumps(dados, indent=4)

        # --- PASSO 5: ESCREVER NO ARQUIVO ---
        # Abrimos o arquivo com o modo "w" (Write - Escrever).
        # Se o arquivo não existe, ele é criado. Se existe, ele é sobrescrito.
        arquivo_aberto = open(self.nome_arquivo, "w")
        
        # Escrevemos o nosso texto organizado lá dentro.
        arquivo_aberto.write(texto_organizado)
        
        # Fechamos o arquivo. É como salvar e fechar o Word.
        arquivo_aberto.close()

        print(f"\n[SISTEMA] O progresso foi salvo com sucesso!")

    # Esta função lê o arquivo e traz os dados de volta para o jogo.
    def carregar(self):
        # Usamos o 'try' para o jogo não fechar sozinho se o arquivo sumir.
        try:
            # Abrimos o arquivo no modo "r" (Read - Ler).
            arquivo_aberto = open(self.nome_arquivo, "r")
            
            # Lemos todo o texto que está gravado lá dentro.
            conteudo_do_texto = arquivo_aberto.read()
            
            # Fechamos o arquivo, já que já pegamos o texto.
            arquivo_aberto.close()

            # Transformamos o TEXTO de volta em 'dados' que o Python entende.
            dados_convertidos = json.loads(conteudo_do_texto)
            
            return dados_convertidos # Devolvemos os dados carregados
        except:
            # Se der erro (tipo arquivo não encontrado), retornamos None (vazio).
            return None
