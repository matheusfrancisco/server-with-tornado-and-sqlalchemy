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

