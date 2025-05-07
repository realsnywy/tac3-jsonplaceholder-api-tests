import pytest
import sys
import os

if __name__ == "__main__":
    print("Iniciando a execução dos testes automatizados...")

    # Define o diretório onde os testes estão localizados (relativo ao project_root)
    test_dir = "test"

    # Argumentos para o pytest. '-v' para verbose, '--log-cli-level=INFO' para ver logs INFO no console
    # Você pode adicionar outros argumentos conforme necessário (ex: '-k' para filtrar testes, '--html=report.html' para relatório)
    args = [
        test_dir,
        "-v",  # Modo verbose
        # "--log-cli-level=INFO" # Garante que logs INFO configurados em conftest apareçam
        # Adicione aqui outros plugins ou argumentos do pytest, se usar.
        # Exemplo: '--html=test_report.html', '--cov=app' (para coverage, requer pytest-cov)
    ]

    # Garante que o diretório raiz esteja no path para importações corretas,
    # especialmente se houver módulos compartilhados fora de 'app' ou 'test'.
    # project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # if project_root not in sys.path:
    #     sys.path.insert(0, project_root)
    # print(f"Project root added to sys.path: {project_root}") # Debug

    # Executa o pytest
    # O pytest é geralmente bom em encontrar o conftest.py na árvore de diretórios
    exit_code = pytest.main(args)

    print(f"Execução dos testes concluída com código de saída: {exit_code}")
    sys.exit(exit_code)
