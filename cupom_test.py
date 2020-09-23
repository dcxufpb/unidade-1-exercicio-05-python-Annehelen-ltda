import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    global nome_loja
    cupom.nome_loja = ""
    verifica_campo_obrigatorio("O campo nome da loja é obrigatório") 
    cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    cupom.logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
    global numero
    cupom.numero = 0
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    numero = 500

def test_municipio_vazio():
    global municipio
    cupom.municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    cupom.municipio = "Campinas"

def test_estado_vazio():
    global estado
    cupom.estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    cupom.estado = "SP"

def test_cnpj_vazio():
    global cnpj
    cupom.cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    cupom.inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Smelly Cat"
    cupom.logradouro = "Rua Etheria"
    cupom.numero = 205
    cupom.complemento = "Perto da velhinha que mora em uma caverna"
    cupom.bairro = "Br. Templo do Cristal"
    cupom.municipio = "Beach City"
    cupom.estado = "BC"
    cupom.cep = "8051-604"
    cupom.telefone = "(66)4002-8922"
    cupom.observacao = "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta"
    cupom.cnpj = "53.409.609/0001-85"
    cupom.inscricao_estadual = "512.670.302.653"

    expected = "Smelly Cat\n"
    expected += "Rua Etheria, 205 Perto da velhinha que mora em uma caverna\n"
    expected += "Br. Templo do Cristal - Beach City - BC\n"
    expected += "CEP:8051-604 Tel (66)4002-8922\n"
    expected += "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta\n"
    expected +="CNPJ: 53.409.609/0001-85\n"
    expected += "IE: 512.670.302.653\n"


    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == expected
