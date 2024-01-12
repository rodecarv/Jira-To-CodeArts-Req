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
            data_codearts = {self.data_codearts} ;
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

    def show_pretty_data(self):
        for i in codearts.data_codearts:
            print(f'\n{i}')
            # j == header
            for j in codearts.data_codearts[i]:
                if codearts.data_codearts[i][j] != '':
                    print(f'   {j} : {codearts.data_codearts[i][j]}')


class TemplateController:
    def __init__(self, final:CodeArtsTemplate, codearts:CodeArtsTemplate, jira:JiraTemplate):
        self.codearts = codearts
        self.jira = jira
        self.final = final

    def jira_to_codearts(self):
        if not self.jira.data_jira:
            self.jira.read_jira_csv()
        if not codearts.data_codearts:
            codearts.read_codearts_csv()

        # final e codearts possuem o mesmo header.
        self.final.header = codearts.header

        # Percorrer o jira, inserindo os respectivos dados no final.
        for index, i in enumerate(self.jira.data_jira):
            current_data = {}
            # Preencher o final.data_codearts com apenas valores vazios.
            for head in self.final.header:
                current_data.update({head : ''})
            # j == header
            for j in self.jira.data_jira[i]:
                if j == 'ï»¿Summary':
                    current_data.update({'Title' : self.jira.data_jira[i][j]})
                if j == 'Issue Type':
                    current_data.update({'Type' : self.jira.data_jira[i][j]})
            
            self.final.data_codearts[index] = current_data

        


def new_table(file_name:str):
    # with open(file_name, mode='w') as file:
    #     # Creating a csv writer object.
    #     csvwriter = csv.writer(file)
    pass


if __name__ == '__main__':
    jira = JiraTemplate(jira_file='jira.csv')    
    codearts = CodeArtsTemplate(codearts_file='codearts.csv')
    final = CodeArtsTemplate(codearts_file='final.csv')
    template_ctl = TemplateController(codearts=codearts, jira=jira, final=final)

    template_ctl.jira_to_codearts()
    print(final)
        