import os # Para manipular diretórios
import pandas as pd # Para trabalhar com DataFrame


# Puxa todos os atributos de cada objeto Fazenda e adiciona em um Data Frame
# Exporta os dados para um csv, para ser usado na análise em R
def export_data_to_csv(registers):
    try:
        # Pega a raiz do projeto (um nível acima da pasta source)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = os.path.join(project_root, "r_analysis", "farm_data.csv")

        # Cria a pasta se não existir
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Cria DataFrame a partir dos atributos e exporta para arquivo csv
        df = pd.DataFrame([
            {
                "agriculture_type": farm.agriculture_type.describe(),
                "area": farm.area,
                "quantity_product": farm.quantity_product
            }
            for farm in registers
        ])
        df = df.round({"area": 2, "quantity_product": 2})
        df.to_csv(filename, index=False)
        print(f"Dados exportados com sucesso para {filename}")

    except Exception as e:
        print(f"Erro ao exportar dados: {e}")

