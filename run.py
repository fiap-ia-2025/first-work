import os
import sys

# Caminho absoluto para o diretório source
source_path = os.path.join(os.path.dirname(__file__), "source")

# Adiciona o caminho à lista de paths do Python
sys.path.insert(0, source_path)

# Importa o main e roda o programa
import main
main.main()

