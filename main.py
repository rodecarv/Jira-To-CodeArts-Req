# TASKS:
# 1. Entender os equivalentes (JIRA e CodeArts).
# 2. Criar o codigo para adaptar do JIRA pro CodeArts

import csv

header_codearts = [] # Array.
data_codearts = [] # Matrix.

header_jira = []
data_jira = [] # Matrix.
# Conseguimos comparar com: data_codearts[data][i] <==> header_codearts[i] 

# Ler o arquivo csv do codearts e guardar os dados em data_codearts.
def read_codearts_csv(file_name:str):

    with open(file_name, mode='r') as file:
        csv_file = csv.reader(file)
        for i, lines in enumerate(csv_file):
            
            # Coletar o header.
            if i == 0:
                for e in lines:
                    header_codearts.append(e)

            # Coletar cada dado.
            else:
                data_codearts.append(lines)

        #print('\t ------ CODEARTS!!!! ------\n')
        #print(f'\nHeader do CodeArts: {header_codearts}\n')
        for i in data_codearts:
            for index, head in enumerate(header_codearts): 
                print(f'{index}: Data[{data_codearts.index(i)}] : {head} : {i[index]}')

# Ler o arquivo csv do Jira e guardar os dados em data_jira.
def read_jira_csv(file_name:str):
    with open(file_name, mode='r') as file:
        csv_file = csv.reader(file)
        for i, lines in enumerate(csv_file):
            
            # Coletar o header.
            if i == 0:
                for e in lines:
                    header_jira.append(e)

            # Coletar cada dado.
            else:
                data_jira.append(lines)

        #print('\t ------ JIRA!!!! ------\n')
        #print(f'\nHeader do JIRA: {header_jira}\n')
        for i in data_jira:
            for index, head in enumerate(header_jira): 
                print(f'{index}: Data[{data_jira.index(i)}] : {head} : {i[index]}')
        
def new_table(file_name:str):
    with open(file_name, mode='w') as file:
    
            

    


if __name__ == '__main__':
    #para preencher com o nome do usuário
    #user_name_hw = input('Type your username: ')
    print(user_name_hw)

    read_codearts_csv('codearts.csv')
    read_jira_csv('jira.csv')
    new_table('modified.csv')
