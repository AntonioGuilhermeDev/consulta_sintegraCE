#BIBLIOTECAS

import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

urllib3.disable_warnings(category=InsecureRequestWarning)

#Scrapping - BeautifulSoup

cabecalho = {"User-Agent": "Opera"}
url = "https://internet-consultapublica.apps.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf="
entrada = str(input("Insira o CNPJ da empresa a ser consultada: "))
urlcomp = url + entrada.replace('.', '').replace('/', '').replace('-', '')
cnpj_req = requests.get(urlcomp, verify=False, headers=cabecalho)
request_status = cnpj_req.status_code
soup = BeautifulSoup(cnpj_req.text, "html.parser")
#print(soup)

#SEPARAÇÃO IDENTIFICAÇÃO

dados = soup.find_all('table', {'id' : 'dadossintegra'})
#print(dados)
dados = (dados[0].contents[3].text)
dadosorg = dados.split('\n')
cnpj = dadosorg[2]
IS = dadosorg[3]
nome = dadosorg[4]

#SEPARAÇÃO ENDEREÇO

enderecohtml = soup.find_all('table' , {'id' : 'enderecosintegara'})
#print(enderecohtml)
endereco = enderecohtml[0].contents[1].text
#print(endereco)
endereco_org = endereco.split('\n')
#print(endereco_org)
logradouro = endereco_org[6]
numero = endereco_org[10]
complemento = endereco_org[12]
bairro = endereco_org[16]
municipio = endereco_org[20]
uf = endereco_org[22]
cep = endereco_org[26]
telefone = endereco_org[28]

#SEPARAÇÃO INFORMAÇÃO COMPLEMENTAR

inf_comp = enderecohtml[1].contents[1].text
#print(ing_comp)
infcomp_org = inf_comp.split('\n')
#print(infcomp_org)
cnae_pri1 = infcomp_org[7]
cnae_pri2 = infcomp_org[8]
cnae_pri2b = " ".join(cnae_pri2.split())
cnae_sec1 = infcomp_org[14]
cnae_sec2 = infcomp_org[15]
cnae_sec2b = " ".join(cnae_sec2.split())
situacao = infcomp_org[20]
data_inicio = infcomp_org[24]
data_situacao = infcomp_org[28]
regime = infcomp_org[32]
credenciamento1 = infcomp_org[36]
credenciamento2 = infcomp_org[37]
obrigadoefd = infcomp_org[41]
data_obriga = infcomp_org[45]
opcao_simples = infcomp_org[49]
obrigadocte = infcomp_org[53]
data_obrigacte = infcomp_org[57]

#RESPOSTA
print('\nIDENTIFICAÇÃO\n' , 'CNPJ:', cnpj, '\nInscrição Estadual:' , IS, '\nNome da empresa:', nome, "\n" , '\nENDEREÇO\n', 'Logradouro:', logradouro, '\nNúmero:', numero, '\nComplemento:', complemento, '\nBairro:', bairro, '\nMunicipio:', municipio, '\nUF:', uf, '\nCEP:', cep, '\nTelefone:', telefone, "\n" ,'\nINFORMAÇÕES COMPLEMENTARES\n' , 'CNAE Fiscal Primário:', cnae_pri1, cnae_pri2b, '\nCNAE Fiscal Secundário:', cnae_sec1, cnae_sec2b, '\nSituação Cadastral Vigente:', situacao, '\nData de Início de Atividade:', data_inicio, '\nData da Situação Cadastral:', data_situacao, '\nRegime de Recolhimento:', regime, '\nCredenciamento antecipado:',credenciamento1, credenciamento2, '\nObrigado a EFD:', obrigadoefd, '\nData Obrigatoriedade EFD:', data_obriga, '\nOpção Simples:', opcao_simples, '\nObrigado a CT-e:', obrigadocte, '\nData Obrigatoriedade CT-e:', data_obrigacte, "\n" , '\nOBSERVAÇÃO: Os dados acima são baseados em informações fornecidas pelo contribuinte, estando sujeitos a posterior confirmação pelo Fisco.')