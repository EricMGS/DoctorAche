# [DoctorAche](https://github.com/ericmgs/DoctorAche)
Um sistema de apoio a decisão (SAD) que auxilia na identificação de uma doença informando os sintomas
  
<img src="https://raw.githubusercontent.com/EricMGS/DoctorAche/master/image.png" alt="Project Image"/>    

ATENÇÃO!!! ESSE É UM PROJETO ACADÊMICO, NÃO USÁ-LO EM SITUAÇÕES REAIS    
  
## Dependências
- [Python 3](https://www.python.org/downloads/)
- PyQt5
  - Digitar no terminal/cmd/prompt/console o seguinte comando:
  ``` pip install PyQt5 ```
  
## Tecnologias
Linguagem de programação: *Python 3*  
Interface gráfica: *PyQt 5*  
Banco de dados: *SQLite 3*  
  
## Como usar
**OBS: NÃO MOVER NEM RENOMEAR NENHUM ARQUIVO, CASO CONTRÁRIO O SISTEMA NÃO FUNCIONARÁ**
  
### Executar programa
Executar o arquivo "/frontend/main.py"

### Esquema de pastas
O projeto está organizado da seguinte forma:
- **backend**
  - *DoctorAche.py* (arquivo principal do programa, é ele que gera os resultados)
  - *spellChecker.py* (corretor ortográfico)
- **database**
  - *database* (banco de dados)
  - *doencas* (arquivo de texto com todos os registros do banco de dados)
  - *scriptInsercaoBD.py* (script para facilitar inserção, remoção e busca de registros individuais no banco de dados)
  - *update.py* (insere todas os registros do arquivo "doencas" no banco de dados)
- **frontend**
  - **img** (imagens usadas na interface)
    - *balao.png*
    - *icon.png*
    - *nurse.png*
  - *main.py*(interface gráfica)
- **teste**
  - *teste.py* (teste de eficiência do programa)
- *LICENSE* 
- *README.md*
- *slides.pptx* 
  
### Adicionar registros
Adicionar registros no arquivo "/database/doencas"  
**OBS: MANTER O PADRÃO DO ARQUIVO, CASO CONTRÁRIO O SISTEMA NÃO FUNCIONARÁ**  
Após isso atualizar o banco de dados executando o arquivo "/database/update.py"

     
  
