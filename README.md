# generate_report

<p>Script Python para criação de relatório com base no JSON de execução do Postman e do Qase.io.</p>
<p>Estes scripts foram criados para resolver o problema do postman não possuir um bom relatório gráfico 
para apresentação em reuniões, etc. Além do sistema gerenciador de casos de teste (Qase.io), que exporta 
os casos de teste em json e outros formatos, mas não em uma collection apresentável para mostrar aos outros 
departamentos ou até mesmo para qualquer um dos stakeholders que não possuem acesso ao sistema.</p>

## Ferramentas utilizadas

- Python 3.12

## Preparação do ambiente
Salve o arquivo json do postman na raiz do projeto com o nome de `results.json` , em seguida, 
certifique-se de ter ativo seu .venv do projeto, execute o comando abaixo para gerar o relatório:

**Comando para gerar o relatório do postman**:

````python
python3 generate_report_postman.py
````

Em seguida, basta abrir o relatório gerado, na raiz do projeto, com o nome de `report.html`

Adicionalmente, criei neste mesmo projeto mais duas funções, separadas em pastas. Um gerador de 
relatórios para o QASE (ferramenta de controle de qualidade de software) e um comparador de 
resultado de consutas SQL. A lógica de funcionamento para o QASE é a mesma.

Quanto ao comparador de resultado de consultas SQL, basta colocar o resultado da consulta 1 e 2 nas 
strings indicadas e rodar o script, ele devolve no console quais são as diferenças entre os resultados.

## Links úteis.

- [Documentação oficial do Python)](https://www.python.org/)
- [Configurar o virtual env do projeto](https://docs.python.org/pt-br/3/library/venv.html)
