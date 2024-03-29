
# Django-React

Ramificação do repositório [hackathon_UFC_2023](https://github.com/agostin-afk/hackathon_UFC_2023)


Nesse repositório já há uma certa integração com a ferramenta React next usando o MUI (material UI) e o django rest-framework.

_Por motivos de segurança, este repositório foi transferido antes do término do projeto para os domínios da UFC, mas você pode ver o resultado em: https://pedidostic.ufc.br/_

## Funcionalidades

- Cadastrar produtos
- Sistema de E-commerce completo (carrinho, finalização de pedido, etc...)
- Envio de Emails de aviso com prazos 
- Sistema de acompanhamento do pedido

## Instalação

Rode esses comandos no terminal da raiz do projeto:

```bash
.\NomeDoSeuAmbienteVirtual\Scripts\Activate.ps1
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
    
## Bibliotecas

Com o ambiente virtual ativado, instale as seguintes dependências antes de rodar os comandos migrate:

```bash
asgiref==3.7.2
certifi==2023.7.22
cffi==1.16.0
charset-normalizer==3.3.0
cryptography==41.0.4
defusedxml==0.7.1
Django==4.2.4
django-allauth==0.57.0
django-cors-headers==4.2.0
django-filter==23.2
djangorestframework==3.14.0
idna==3.4
Markdown==3.4.3
oauthlib==3.2.2
Pillow==10.0.1
psycopg2==2.9.7
pycparser==2.21
PyJWT==2.8.0
python-dotenv==1.0.0
python3-openid==3.2.0
pytz==2023.3
requests==2.31.0
requests-oauthlib==1.3.1
scapy==2.5.0
sqlparse==0.4.4
tzdata==2023.3
urllib3==2.0.6
```
## Usado por

Esse projeto é usado pela UFC.


