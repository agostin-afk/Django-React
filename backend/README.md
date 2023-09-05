
# backend carnaúba

As tecnologias utilizadas foram:
    Django, djangorestframework

atualmente apenas os modelos e as rotas default foram criadas. Próximo passo é refinar os modelos, caso necessário, e aplicar as regras de negócio. 



## Instruções para Usar

verifique se o python está instalado na máquina. versão recomendada: python 3.11 ou superior.

com o python instalado, crie um ambiente virtual.
instale o virtualenv -> pip install virtualenv

crie um ambiente virutal -> virtualenv venv .

ative o ambiente virtual -> venv/Scripts/activate

## Instalando o django
Com o ambiente virtual ativado, faça:
pip install Django

Depois execute o comando para instalar as dependências
pip install -r requirements.txt

por fim, suba o servidor
python .\manager.py runserver