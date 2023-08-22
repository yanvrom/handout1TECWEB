import json
import codecs

def extract_route(requisicao:str):
    rota = requisicao.split()[1][1:]
    return rota

def read_file(path):
    conteudo = open(path, "r+b").read()
    return conteudo

def load_data(nome_arquivo_json):
    with open("data/" + nome_arquivo_json, encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados

def load_template(nome_arquivo_template):
    template = open("templates/"+nome_arquivo_template, "r").read()
    return template

def add_anotacao(titulo, detalhes):
    notes:list = load_data("notes.json")
    notes.append({"titulo":titulo, "detalhes":detalhes})
    with open("data/notes.json","w" ,encoding='utf-8') as meu_json:
        meu_json.write(str(notes).replace("'", "\""))

def build_response(body='', code=200, reason='OK', headers=''):
    'HTTP/1.1 200 OK\n\n'
    if headers == '':
        retornar = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body
    else:
        retornar = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers + '\n\n' + body
    return retornar.encode()