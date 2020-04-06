# Instalando

Com o projeto já baixado, você deve acessar o diretório e executar o comando abaixo para criar um ambiente virtual.

`python -m venv .venv`

Quando o ambiente for criado, acesse-o usando o comando abaixo:

`source .venv/bin/activate`

E se você estiver no windows, dentro do powershell execute:

`.venv/Scripts/Activate.ps1`

Agora você deve instalar todas as depêndencias:

`(.venv) $ pip install -r requirements.txt`

# Usando

Quando concluir, você pode executar o comando `flask vue watch` para que o `webcpack` 
fique escutando todas as modificações no diretório frontend.

Abra uma outra aba no terminal e então execute o comando abaixo para rodar o flask.

`flask run`

Não esqueça que para executar o comando acima, você deve acessar o ambiente virtual como mostrado anteriormente.
