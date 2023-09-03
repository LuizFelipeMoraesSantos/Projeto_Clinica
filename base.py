# Criar um arquivo ou adicionar novos parâmetros
arquivo_cadastro = open("cadastro.txt", "a")
arquivo_cadastro.close()

arquivo_marcacao = open("marcacao.txt", "a")
arquivo_marcacao.close()

# Função para cadastrar paciente
def cadastrar_paciente():
    nome = input('Cadastre o nome: ')
    telefone = input('Cadastre o telefone (0000-0000): ')

    # Abrir arquivo cadastro.txt para leitura e percorrer todas as linhas para verificar se o paciente já está cadastrado
    arquivo = open("cadastro.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        dados = linha.strip().split(',')
        nome_cadastrado, telefone_cadastrado = dados[0], dados[1]
        if telefone == telefone_cadastrado:
            print("Paciente já cadastrado!")
            return

    # Abrir arquivo cadastro.txt em modo de escrita e escrever no arquivo o nome e telefone do paciente
    arquivo = open("cadastro.txt", "a")
    arquivo.write(f'{nome},{telefone}\n')
    arquivo.close()

# Função para marcar consulta
def marcar_consulta():
    # Abrir arquivo cadastro.txt para leitura e percorrer todas as linhas para exibir os pacientes cadastrados
    arquivo_cadastro = open("cadastro.txt", "r")
    linhas_cadastro = arquivo_cadastro.readlines()
    arquivo_cadastro.close()
    # Se não houver nem um paciente cadastrado retornar ao menu para cadastrar.
    if not linhas_cadastro:
        print('Nenhum paciente cadastrado.')
        return
    # lista de pacientes para ajudar na procura do paciente para marcação.
    print('Pacientes cadastrados:')
    for c, linha in enumerate(linhas_cadastro, 1):
        dados = linha.strip().split(',')
        nome = dados[0]
        print(f'{c}. {nome}')

    # Abrir arquivo marcacao.txt para leitura e percorrer todas as linhas para verificar se a consulta já está marcada
    arquivo_marcacao = open("marcacao.txt", "r")
    linhas_marcacao = arquivo_marcacao.readlines()
    arquivo_marcacao.close()
    #Se não houver nem uma consulta marcada no arquivo.
    if not linhas_marcacao:
        print('Nenhuma consulta marcada.')

    nome = input('Digite o nome do paciente: ')
    data = input('Data (DD/MM/AAAA): ')
    hora = input('Hora (HH:MM): ')
    especialista = input('Especialidade do médico: ')
    # retirei dados[1] e dados[2] e atribui a variavel marcacao_data e marcacao_hora.
    for linha in linhas_marcacao:
        dados = linha.strip().split(',')
        marcacao_data = dados[1]
        marcacao_hora = dados[2]

        # fiz a compração para ver se existia marcaçao nessa data e hora, se houver parar.
        if marcacao_data == data and marcacao_hora == hora:
            print("Já existe uma marcação nesse horário e data.")
            break
    # Se nao houver horarios e datas iguais, registrar no arquivo marcacao.txt
    else:
        arquivo_marcacao = open("marcacao.txt", "a")
        arquivo_marcacao.write(f'{nome},{data},{hora},{especialista}\n')
        arquivo_marcacao.close()
        print("Consulta marcada com sucesso!")

# Função para cancelar consulta
def cancelar_consulta():
    nome = input('Digite o nome do paciente para cancelar a consulta: ')

    # Abrir arquivo marcacao.txt para leitura
    arquivo_marcacao = open("marcacao.txt", "r")
    linhas_marcacao = arquivo_marcacao.readlines()
    arquivo_marcacao.close()

    #lista vazia
    encontradas = []

    # Se linha estiver dentro de linhas_marcação
    # dividir a lista nas virgulas e peguei os dado[0], se for iqual ao nome adicione na lista encontrados a linha
    for linha in linhas_marcacao:
        dados = linha.strip().split(',')
        if dados[0] == nome:
            encontradas.append(linha)
    #se encontrados for verdadeiro , abra o arquivo marcacao.txt e escreva "w" que vai apagar a marcação.
    # escrevendo arquivo_macacao em linha.
    if encontradas:
        arquivo_marcacao = open("marcacao.txt", "w")
        for linha in linhas_marcacao:
            if linha not in encontradas:
                arquivo_marcacao.write(linha)
        arquivo_marcacao.close()
        print("Consulta cancelada!")
    else:
        print('Essa marcação não existe.')
# looping sempre verdadeiro para fazer  o cadastro até escolher sair do programa
while True:
    print('\033[34m-=-' * 10)
    print('     Clínica Ágil     ')
    print('-=-' * 10)

    print('''
[1] Cadastrar paciente
[2] Marcar consulta
[3] Cancelamento de consulta
[4] Sair\033[m''')
    escolha = (input("   \033[31mEscolha uma opção:\033[m "))
#escolha o numero, para ir na funçao desejada usando condicionais.
    if escolha == '1':
        cadastrar_paciente()
    elif escolha == '2':
        marcar_consulta()
    elif escolha == '3':
        cancelar_consulta()
    elif escolha == '4':
        print('Saindo...')
        break
    elif escolha != '1' or escolha != '2' or escolha != '3' or escolha != '4':
        print('Opção inválida!!!!')