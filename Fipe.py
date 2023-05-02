import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelo = self.get_modelos()
        
    def __iter__(self):
        self.index = 0 
        return self
    
    def __next__(self):
        if self.index >= len(self.modelo):
            raise StopIteration
        modelo = self.modelo[self.index]
        self.index += 1
        return {'nome': modelo['nome'], 'id': modelo['codigo']}
    
    def get_modelos(self):
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos"
        response = requests.get(url)
        modelos = response.json()['modelos']
        return modelos
    
def listar_codigos_marcas():
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    response = requests.get(url)
    marcas = response.json()
    for marca in marcas:
        print(f"{marca['codigo']} - {marca['nome']}")
            
def buscar_veiculos(marca_id):
    iterator = FipeIterator(marca_id)
    veiculos = []
    for modelo in iterator:
        veiculos.append(modelo)
    return veiculos
        
print('Lista de IDs das marcas disponiveis:')
listar_codigos_marcas()
    
marca_id = int(input('Digite o ID de uma marca: '))
veiculos = buscar_veiculos(marca_id)
print('veiculos da marca selecionada:')
#print(veiculos)

for veiculo in veiculos:
    print(f'Nome: {veiculo["nome"]}')