# IMPORTANTE:
# Este script assume que você está rodando a partir da pasta 'r_analysis'
# e que o arquivo 'farm_data.csv' está nesta mesma pasta.

# Garantir que o pacote de manipulação de dados esteja instalado
if (!require(dplyr)) {
  install.packages("dplyr")
  library(dplyr)
} else {
  library(dplyr)
}

# Importar os dados das plantações e exibi-los
farm_data <- read.csv("r_analysis/farm_data.csv")
print(farm_data)

# Transformar 'agriculture_type' e 'farm_name' em fator para análise categórica
farm_data$agriculture_type <- as.factor(farm_data$agriculture_type)
farm_data$farm_name <- as.factor(farm_data$farm_name)

# Criar nova variável de insumo por m² (Densidade)
farm_data$input_per_m2 <- farm_data$quantity_product/farm_data$area

# Gerar estatísticas descritivas agrupadas por tipo de cultura
summary_stats <- farm_data %>%
  group_by(agriculture_type, farm_name) %>%
  summarise(
    n = n(),                              # Contagem de observação por grupo
    avg_area = mean(area),                # Média da área plantada
    sd_area = ifelse(n() > 1, sd(area), 0), # Desvio padrão da área (Se tiver só 1 observação, assume 0)
    avg_input = mean(quantity_product),  # Média de insumo necessário
    sd_input = ifelse(n() > 1, sd(quantity_product), 0),  # Desvio padrão do insumo (Se tiver só 1 observação, assume 0)
    avg_input_per_m2 = mean(input_per_m2)   # Eficiência de insumo por m²
  )

# Exibir o resumo estatístico no console
print(summary_stats)
