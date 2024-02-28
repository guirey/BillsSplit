# inicialização de bibliotecas e definição de tema

import PySimpleGUI as sg
import tabulate


sg.set_options(font=("Consolas", 12))  # define a fonte padrao como consolas (monoespaçada)
sg.theme('Green Mono')  # definindo o tema das janelas

# In[111]:


# janela que recebe os dados do usuario e calcula a proporçao das rendas

layout = [[sg.Text('Qual a renda da pessoa 1?')],
          [sg.InputText()],
          [sg.Text('Qual a renda da pessoa 2?')],
          [sg.InputText()],
          [sg.Submit('isso'), sg.Cancel('num kero')]]

window = sg.Window('Mozidex', layout, keep_on_top=True, grab_anywhere=True)

event, values = window.read()
window.close()

pessoa1 = float(values[0])
pessoa2 = float(values[1])

total = pessoa2 + pessoa1

proporcaoPessoa1 = pessoa1 / total
proporcaoPessoa2 = pessoa2 / total

proporcaoPessoa1 = pessoa1 / total * 100
proporcaoPessoa2 = pessoa2 / total * 100

texto_proporcao = f'''A proporção de renda é de:
pessoa1: {proporcaoPessoa1:,.2f}% e pessoa2: {proporcaoPessoa2:,.2f}%'''

# In[112]:


# janela que recebe dados do usuario com valor das contas

layout = [[sg.Text('Valor de Despesas com a Residência:')], [sg.InputText()],
          [sg.Text('Valor de Despesas com Água:')], [sg.InputText()],
          [sg.Text('Valor de Despesas com Energia Elétrica:')], [sg.InputText()],
          [sg.Text('Valor de Despesas com Internet:')], [sg.InputText()],
          [sg.Submit('isso'), sg.Cancel('num kero')]]

window = sg.Window('Mozidex', layout, keep_on_top=True, grab_anywhere=True)

event, values = window.read()
window.close()

casa = float(values[0])
agua = float(values[1])
luz = float(values[2])
internet = float(values[3])

reservaPessoa1 = 0.1 * pessoa1
reservaPessoa2 = 0.1 * pessoa2

pessoalPessoa1 = 0.05 * pessoa1
pessoalPessoa2 = 0.05 * pessoa2

investPessoa1 = 0.05 * pessoa1
investPessoa2 = 0.05 * pessoa2

totalPessoa1 = reservaPessoa1 + pessoalPessoa1 + investPessoa1 + (casa * proporcaoPessoa1) + (agua * proporcaoPessoa1) + (
            luz * proporcaoPessoa1) + (internet * proporcaoPessoa1)
totalMo = reservaPessoa2 + pessoalPessoa2 + investPessoa2 + (casa * proporcaoPessoa2) + (agua * proporcaoPessoa2) + (luz * proporcaoPessoa2) + (
            internet * proporcaoPessoa2)

# regra de divisao:
# 50% do salario = contas fixas
# 30% = custos variaveis (lazer, delivery, gás, etc)
# 10% = reserva emergencial do casal
# 5% = investir
# 5% = gastos individuais


# In[113]:


# create data
data = [["Aluguel", casa * proporcaoPessoa1, casa * proporcaoPessoa2],
        ["Água", agua * proporcaoPessoa1, agua * proporcaoPessoa2],
        ["Energia", luz * proporcaoPessoa1, luz * proporcaoPessoa2],
        ["Internet", internet * proporcaoPessoa1, internet * proporcaoPessoa2],
        ["Reserva", reservaPessoa1, reservaPessoa2],
        ["Pessoal", investPessoa1, investPessoa2],
        ["Investimento", investPessoa1, investPessoa2],
        ["Total", totalPessoa1, totalPessoa2]]

# define header names
col_names = ["Despesas", "Pessoa1", "Pessoa2"]

# display table
resultado = tabulate.tabulate(data, headers=col_names, stralign="center", numalign="center", tablefmt="fancy_grid")

texto_contas = f'''A proporção de renda é de:
{resultado}
'''

# In[114]:


# janela que mostra o resultado da proporção das contas

event, values = sg.Window('Janela do Amor',
                          [[sg.T(f'{texto_contas}')],
                           [sg.Cancel('sair')]], keep_on_top=True, element_justification='c').read(close=True)

if event == sg.WIN_CLOSED or event == 'sair':
    pass

window.close()

# In[115]:


# janela que mostra o resultado da proporção das rendas

event, values = sg.Window('Janela do Amor',
                          [[sg.T(f'{texto_proporcao}')],
                           [sg.Cancel('sair')]], keep_on_top=True, element_justification='c').read(close=True)

if event == sg.WIN_CLOSED or event == 'sair':
    pass

window.close()





