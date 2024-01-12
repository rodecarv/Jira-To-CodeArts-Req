# TASKS:
# 1. Entender os equivalentes (JIRA e CodeArts).
# 2. Criar o codigo para adaptar do JIRA pro CodeArts

import csv

header_codearts = [] # Array.
data_codearts = [] # Matrix.

class JiraTemplate:
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
                    current_line.update({head : i[index]})
                self.data_jira[data.index(i)] = current_line
    
    def show_pretty_data(self):
        for i in jira.data_jira:
            print(f'\n{i}')
            # j == header
            for j in jira.data_jira[i]:
                if jira.data_jira[i][j] != '':
                    print(f'   {j} : {jira.data_jira[i][j]}')


class CodeArtsTemplate:
    def __init__(self, codearts_file:str):
        self.header = []
        self.data_codearts = {}
        self.codearts_file = codearts_file

    def __repr__(self):
        return f"""JiraTemplate(
            header = {self.header} ;
            data_codearts = {self.data_jira} ;
            codearts_file = {self.codearts_file}
        )"""

    def read_codearts_csv(self):
        with open(self.codearts_file, mode='r') as file:
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
                    current_line.update({head : i[index]})
                self.data_codearts[data.index(i)] = current_line

    def show_pretty_data():
        for i in codearts.data_codearts:
            print(f'\n{i}')
            # j == header
            for j in codearts.data_codearts[i]:
                if codearts.data_codearts[i][j] != '':
                    print(f'   {j} : {codearts.data_codearts[i][j]}')


class TemplateController:
    def __init__(self, codearts:CodeArtsTemplate, jira:JiraTemplate):
        self.codearts = codearts
        self.jira = jira

def new_table(file_name:str):
    # with open(file_name, mode='w') as file:
    #     # Creating a csv writer object.
    #     csvwriter = csv.writer(file)
    pass


if __name__ == '__main__':
    jira = JiraTemplate(jira_file='jira.csv')
    jira.read_jira_csv()
    
    codearts = CodeArtsTemplate(codearts_file='codearts.csv')
    codearts.read_codearts_csv()

    print('\nJIRA:')
    # i == chave dos dicionarios dentro do dicionario.
    jira.show_pretty_data()

    print('\nCODEARTS:')
    codearts.show_pretty_data()
        