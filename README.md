# Web Server with tornado

# Como rodar o app
Para você rodar a aplicação no tornado:
Utilize um virtualenv para instalar as dependencias
```
pip install -r requeriments.txt
```
Para subir o banco de dados

```
docker-compose up
```
Para rodar as migração:

```
python upgrade head
```

Para rodar a aplicação:

```
python app.py
```

Para realizar post/get/put/delete
```

url post : http://localhost:8000/farm
objeto: {"name": "FAZENDA_1", "latitude": -9.1, "longitude": -45.9333}

url get by id: http://localhost:8000/farm
obj : {"id": numero do id da fazenda}

url put by id: http://localhost:8000/farm
obj : {"id":id_da_fazenda, "name": "FAZENDA_2", "latitude": 2, "longitude": 20}

url put by id: http://localhost:8000/farm
{"id": numero_do_id_da_fazenda}

url delete : http://localhost:8000/farm
{"id": id_fazenda}

```
Na pasta scripts existe um script para tratamento dos dados
python script/script.py

## TODO
- [x] Utilizar um sistema de migração para o banco
- [x] Montar a estrutura das pastas (adpater, domain, models, application)
- [x] Implementar um minimo CRUD para Fazendas
- [ ] Escrever testes unitarios
- [ ] Escrever os testes de integração
- [ ] Tentar utilizar TDD na regra de negocio
- [ ] Utilizar corretamente os status code no servidro (200, 404, 500..)
- [ ] Criar uma tabela para manter outras informações das fazendas
- [ ] Escrever o Readme em ENG também
- [ ] Refatorar o codigo duplicado
- [ ] Remover variaveis de ambiente como URL de banco, etc.. Olhar o site https://12factor.net/
- [ ] Criar uma camada de infra para colcoar coisas do banco de dados como, abrir session e connection com engine
