

def gerador_id():
    IDS = "/home/mrminetoons/Documents/Api-Control/IdGenerator/ids.txt"
    arquivo = open(IDS, "rt") # Inicia o TXT para READ
    ###
    id_atual = arquivo.read() #Abre e adiciona o valor em id_atual
    arquivo.close()
    ###
    id_atual_int = int(id_atual) #Transforma em Inteiro e salva em id_atual_int
    ###
    id_novo_int = id_atual_int+1 #Soma +1 na variavel id_novo_int
    id_novo_str = str(id_novo_int) #Transforma em STR novamente
    ###
    arquivo_para_write = open(IDS, "w+") # Inicia o TXT para WRITE
    arquivo_para_write.write(id_novo_str)
    arquivo_para_write.close()
    ###
    arquivo = open(IDS, "rt") # Inicia o TXT para READ, novamente
    clienteID = arquivo.read()
    arquivo.close()
    return clienteID
