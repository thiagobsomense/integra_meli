# Integra Meli

Aplicativo desenvolvido em Python para integração com Api do Mercado Livre


## Instalação do Projeto no Servidor PythonAnyWhere

Acesse o terminal do PythonAnyWhere e crie uma nova pasta para receber o projeto

```bash
    mkdir integra_meli
```

Acesse a pasta e realize o download desse projeto

```bash
    cd integra_meli
    git clone https://github.com/thiagobsomense/integra_meli.git .
```

Selecione o branch que deseja rodar

```bash
    git checkout development
```


## Instalação

Crie um ambiente virtual para instalar as dependências do projeto 

```bash
    python -m venv env
```

Ative seu ambiente virtual

```bash
    # para sistemas opercaionais UNIX (Linux e MacOS)
    source env/bin/activate

    # para sistemas opercaionais DOS (Windows)
    . env\Scripts\activate
```

Instale todas as dependências

```bash
    pip install -r requirements.txt
```


## Criação da Base de Dados

Acesse a aba "Databases" do PythonAnyWhere e crie sua nova base de dados, logo após crie uma senha para acessar essa base de dados.

Acesse o terminal MySql do PythonAnyWhere e rode o script "db_init.sql".


## Primeiros Passos

Atualize o arquivo ".env.example" com os dados de acesso de banco de dados e demais informações solicitadas e o salve como ".env".

Acesse a pasta principal do projeto e depois já poderá sodar os camandos do arquivo 
"main.py"

```bash
    cd src
```
