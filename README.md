# DoctorAche
Um sistema de apoio a decisão (SAD) que auxilia na identificação de uma doença informando os sintomas

## Dependências
- (Python 3)[https://www.python.org/downloads/]
- PyQt5
  - Digitar no terminal/cmd/prompt/console o seguinte comando:
  ``` pip install PyQt5 ```

## Tecnologias
Linguagem de programação: Python
Interface gráfica: PyQt5
Banco de dados: SQLite

## Como usar
**OBS: NÃO MOVER NEM RENOMEAR NENHUM ARQUIVO, CASO CONTRÁRIO O SISTEMA NÃO FUNCIONARÁ**

### Esquema de pastas
O projeto está organizado da seguinte forma:
- backend
  - DoctorAche.py (arquivo principal do programa, é ele que gera os resultados)
  - spellChecker.py (corretor ortográfico)
- database
  - database (banco de dados)
  - doencas (arquivo de texto com todos os registros do banco de dados)
  - scriptInsercaoBD.py (script para facilitar inserção, remoção e busca de registros individuais no banco de dados)
  - update.py (insere todas os registros do arquivo "doencas" no banco de dados)
- frontend
  - img (imagens usadas na interface)
    - balao.png
    - icon.png
    - nurse.png
  - main.py(interface gráfica)

### Executar programa
Executar o arquivo "/frontend/main.py"

### Adicionar registros
Adicionar registros no arquivo "/database/doencas"
**OBS: MANTER O PADRÃO DO ARQUIVO, CASO CONTRÁRIO O SISTEMA NÃO FUNCIONARÁ**
Após isso atualizar o banco de dados executando o arquivo "/database/update.py"

     
  
