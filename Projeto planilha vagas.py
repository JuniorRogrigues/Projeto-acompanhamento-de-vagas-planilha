import openpyxl

# Criação da planilha
workbook = openpyxl.Workbook()
# Excluir um sheet(página)
del workbook['Sheet']
# Nova sheet
workbook.create_sheet('Vagas')
# Selecionando uma sheet para trabalhar
sheet_vagas = workbook['Vagas']
sheet_vagas.append(['EMPRESA', 'VAGA', 'DATA DA APLICAÇÃO', 'RETORNO'])
# Preenchimento dinâmico das planilhas
continuar = 's'
while continuar == 's':
    empresa = input('Nome da empresa: ')
    vaga = input('Nome da vaga: ')
    data_da_aplicacao = input('Data da aplicação: ')
    retorno = input('Retorno da empresa: ')
    sheet_vagas.append([empresa, vaga, data_da_aplicacao, retorno])
    continuar = input('Deseja continuar o preenchimento? (s/n)')

# Salvando planilha
workbook.save('Acompanhamento de Vagas.xlsx')
