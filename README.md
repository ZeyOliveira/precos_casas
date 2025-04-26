[![author](https://img.shields.io/badge/Zeygler&nbsp;Oliveira-red.svg)](https://www.linkedin.com/in/zeygler-oliveira-a021a92a4/)
[![](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

# California Housing Prices 🏡

Este repositório contém análises e insights baseados no conjunto de dados **California Housing Prices**, disponível no Kaggle. Esse dataset fornece informações sobre preços medianos de casas em distritos da Califórnia, utilizando dados do censo de 1990. Ele é amplamente utilizado para experimentação em aprendizado de máquina, regressão e visualização de dados.
[Link original para o dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

<p align="center"> 
  <a href="https://www.linkedin.com/in/zeygler-oliveira-a021a92a4/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
</p>

![geomap](https://github.com/ZeyOliveira/precos_casas/blob/master/relatorios/imagens/analise_geo.png)

## Conteúdo
- Descrição dos dados disponíveis 📑: `01_dicionario_de_dados.md`


## Objetivo
O propósito deste projeto é investigar padrões de preços de habitação na Califórnia, explorando fatores como localização geográfica, população e renda média. A partir dessas análises, buscamos construir modelos preditivos para estimar valores imobiliários com base nos atributos fornecidos.


##  Uma análise do mercado imobiliário na Califórnia: o que os dados me contaram?  

Quando comecei a explorar os dados do *California Housing Prices*, achei que ia ser só um monte de números sobre casas. Mas aí, comecei a perceber umas tendências que fizeram MUITO sentido no mundo real!  

### **Quanto mais perto do mar, mais caro!**
Uma das primeiras coisas que me chamou atenção foi que as casas mais perto do oceano costumam ter preços bem mais altos. Faz sentido, né? Quem não quer acordar vendo o mar, sentir aquela brisa boa e ainda estar perto de praias famosas? Além da vista, tem a questão da valorização: lugares bonitos e disputados acabam ficando mais caros porque todo mundo quer morar lá. Afinal, quem não gostaria de acordar todos os dias com o som das ondas? 

### **Dinheiro chama dinheiro**
Outra coisa interessante foi perceber que existe uma relação entre a renda da população e o preço das casas. Onde a renda média é mais alta, os preços dos imóveis também sobem. Isso pode estar ligado à infraestrutura, segurança e serviços disponíveis nessas regiões. Ou seja, se o bairro tem escolas boas, comércio forte e qualidade de vida top, ele se torna mais exclusivo e, claro, mais caro.  

### O que isso me ensinou?  
Antes, eu via preço de casa como algo meio aleatório, mas depois dessa análise percebi que dá pra entender muita coisa com números e padrões. Esses dados mostram um pouco de como o mercado imobiliário funciona na Califórnia, e dá pra usar isso pra prever preços, analisar investimentos e até entender melhor como cidades evoluem. Com o avanço das cidades e o aumento da demanda por locais privilegiados, essa relação entre localização, renda e valorização do imóvel provavelmente permanecerá como um dos pilares do setor. 



## Organização do projeto

```
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git Por padrão, o arquivo `.gitignore` já está configurado para ignorar arquivos de dados e
                          arquivos de Notebook (para aqueles que usam ferramentas como
                          [Jupytext](https://jupytext.readthedocs.io/en/latest/) e similares).    


├── requirements.txt       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|      └── auxiliares.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|      └── models.py  <- Scripts utilizados para criar, treinar, testar e organizar modelos de ML  
| 
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.

    a. Caso esteja utilizando o `conda`, exporte as dependências do ambiente para o arquivo `requirements.txt`:

      ```bash
      conda env export > requirements.txt
      ```

Para mais informações sobre como usar Git e GitHub, [clique aqui](https://cienciaprogramada.com.br/2021/09/guia-definitivo-git-github/). Sobre ambientes virtuais, [clique aqui](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/).
