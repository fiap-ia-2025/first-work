# FIAP - Inteligência Artificial
## Cap 1 - Play na sua carreira em IA

### Projeto: FarmTech Solutions


* Culturas escohidas: Soja e Cana de Açucar


| Soja                                                                                                                                                                                          | Cana de Açucar                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| A soja é o principal produto da agricultura brasileira. O Brasil representa cerca de 50% do comércio mundial de soja.  E a região Centro-Oeste é a segunda maior produtora de soja do Brasil. | O Brasil é o maior exportador mundial de açúcar e esse produto gera bilhões de reais de receita.  |
| <img alt="Soja" src="./img/soja.jpeg" width="320" height="205" />                                                                                                                             | <img alt="Cana de Açucar" src="./img/cana.jpg" width="320" height="205" />                        |

**Espaçamento entre plantas**:
1. A distância entre plantas na linha pode variar de 5 a 16 cm. 
2. O espaçamento entre linhas de uma lavoura de soja é recomendado de 40 a 60 cm.

**Escolhas do grupo**:

* Tipo de figura geométrica: Retângulo
  * Para calcular a área de um retângulo: A = B * H 
* Produto para o plantio: Água, 620mm (milímetros) por planta
  * 1 mm = 1l/m2
  * 620mm = 620l/m2
* Distância entre as plantas: 10 cm ou 0.1m
* Espaço entre as linhas das lavoura: 50cm ou 0.5m

**Entregas:**

1. O código fonte em Python para o cálculo da área e do manejo de insumos das Lavouras de Soja e Cana de Açucar podem ser encontrados em: [agriculture.py](source/main.py).
2. O código fonte em R para cálculo de dados estatísticos básicos pode ser encontrado em: ESPECIFICAR APÓS.

### Referências:

1. Como estimar a produtividade na cultura da soja? : https://www.pioneer.com/br/blog/artigos/estimar-produtividade-soja.html
2. Plantio : https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/cana/producao/manejo/plantio

## 📊 Módulo de Análise Estatística em R

Após a coleta e exportação dos dados pelo programa Python, foi desenvolvido um módulo em R para realizar análises estatísticas básicas por tipo de cultura.

### 🔍 O que esse módulo faz:
- Lê os dados do CSV gerado pela aplicação Python.
- Calcula, para cada cultura:
  - Média e desvio padrão da área plantada
  - Média e desvio padrão do insumo necessário
  - Média e desvio padrão da densidade de insumo por metro quadrado (input_per_m2)
  - Coeficiente de variação do insumo utilizado

### 🧠 Interpretação dos resultados:
Essas métricas ajudam o agricultor a:
- Entender o perfil médio das fazendas por cultura
- Avaliar a variabilidade nos dados (se estão padronizados ou não)
- Refletir sobre a eficiência no uso de insumos

### ⚠️ Limitações (importante para interpretação correta):
- Culturas diferentes usam insumos diferentes (ex: Soja usa água, Cana usa nitrogênio).
- Como os dados são agrupados apenas por tipo de cultura, **os valores de insumo e densidade não devem ser comparados diretamente entre culturas**.
- Essa abordagem é suficiente para o escopo atual, mas pode ser expandida com colunas de tipo de insumo no futuro para maior robustez.



