# TASKS:
# 1. Entender os equivalentes (JIRA e CodeArts).
# 2. Criar o codigo para adaptar do JIRA pro CodeArts

import csv

header_codearts = [] # Array.
data_codearts = [] # Matrix.

class JiraTemplate():
    def __init__(self, jira_file:str):
        self.header = []
        self.data_jira = {}
        self.jira_file = jira_file

    def __repr__(self):
        return f"""JiraTemplate(
            header = {self.header} ;
            data_jira = {self.data_jira} ;
            jira_file = {self.jira_file}
        )"""

    def read_jira_csv(self):
        with open(self.jira_file, mode='r') as file:
            csv_file = csv.reader(file)
            data = []
            for i, lines in enumerate(csv_file):
                # Coletar o header.
                if i == 0:
                    for e in lines:
                        self.header.append(e)
                # Coletar cada dado.
                else:
                    data.append(lines)

            for i in data:
                current_line = {}
                for index, head in enumerate(self.header): 
                    #print(f'{index}: Data[{data.index(i)}] : {head} : {i[index]}')
                    current_line.update({head : i[index]})
                self.data_jira[data.index(i)] = current_line
                    

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


def new_table(file_name:str):
    # with open(file_name, mode='w') as file:
    #     # Creating a csv writer object.
    #     csvwriter = csv.writer(file)
    pass


if __name__ == '__main__':
    jira = JiraTemplate(jira_file='jira.csv')
    jira.read_jira_csv()
    
    # i == chave dos dicionarios dentro do dicionario.
    for i in jira.data_jira:
        print(i)
        # j == header
        for j in jira.data_jira[i]:
            if jira.data_jira[i][j] != '':
                print(f'   {j} : {jira.data_jira[i][j]}')
        