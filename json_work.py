"""
**write_json(name_json, kwargs):
Abre um arquivo JSON existente para leitura. Se o arquivo não existir, cria um novo com um dicionário vazio.
Adiciona novos dados ao dicionário existente, agrupando valores sob as chaves fornecidas.
Escreve o dicionário atualizado de volta ao arquivo JSON, formatado com indentação.

**read_json_keys(name_json, *keys)**:
Abre um arquivo JSON para leitura. Se o arquivo não existir, retorna um dicionário com listas vazias para cada chave solicitada.
Extrai e retorna os valores associados às chaves fornecidas do primeiro dicionário na lista do arquivo JSON.

delete_json(name_json):
Tenta excluir o arquivo JSON especificado. Se o arquivo não for encontrado, imprime uma mensagem de erro.
"""
import json
import os 
def write_json(name_json, **kwargs):
    try:
        with open(name_json, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = [{}]

    for key, value in kwargs.items():
        existing_data[0].setdefault(key, []).append(value)

    with open(name_json, 'w') as f:
        json.dump(existing_data, f, indent=4)

def read_json_keys(name_json, *keys):
    try:
        with open(name_json, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                return {key: data[0].get(key, []) for key in keys}
            return {key: [] for key in keys}
    except FileNotFoundError:
        return {key: [] for key in keys}

def delete_json(name_json):
    try:
        os.remove(name_json)
    except FileNotFoundError:
        print(f"Arquivo {name_json} não encontrado.")

if __name__ == '__main__':
    json_id_order = 'id_order.json'
    json_tick     = 'data_tick.json'

    # SAVE DATA
    write_json(json_id_order, id_ordem='12323432432')
    write_json(json_tick, bid='11', ask='11', timestamp='22132130')

    # READ DATA
    result_tick = read_json_keys(json_tick, "bid", "ask", "timestamp")
    result_id   = read_json_keys(json_id_order, "id_ordem")["id_ordem"] 
    print(result_id)
    # VISUALIZE DATA
    for i in range(len(result_tick["bid"])):
        print("bid_go : ",  result_tick["bid"][i])
        print("ask_go : ",  result_tick["ask"][i])
        print("timestamp:", result_tick["timestamp"][i])

    for i in range(len(result_id)):
        print("id_ordem:", result_id[i],type(result_id[i]))

    # DELETE JSON FILES
    com = int(input("Press 1 to delete json files: "))
    if com == 1:
        # DELETE JSON FILES
        delete_json(json_id_order)
        delete_json(json_tick)
