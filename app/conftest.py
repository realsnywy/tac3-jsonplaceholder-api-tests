import pytest
import logging
import sys
import os

# --- Configuração do Logging ---

# Garante que o diretório de logs exista (opcional, pode logar no console)
# log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
# os.makedirs(log_dir, exist_ok=True)
# log_file = os.path.join(log_dir, 'test_run.log')

# Configura o logging básico
# Formato: Nível - Timestamp - Nome do Logger - Mensagem
log_format = "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
logging.basicConfig(
    # filename=log_file, # Descomente para logar em arquivo
    level=logging.INFO,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,  # Loga no console por padrão
)

# Cria um logger específico para os testes de API
api_logger = logging.getLogger("api_tests")
api_logger.setLevel(logging.INFO)  # Define o nível do logger específico

# Adiciona um handler para garantir a saída (se não usar basicConfig com stream)
# handler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter(log_format)
# handler.setFormatter(formatter)
# if not api_logger.handlers:
#     api_logger.addHandler(handler)


# --- Fixtures do Pytest ---


@pytest.fixture(scope="session")
def base_url():
    """Fixture que retorna a URL base da API JSONPlaceholder."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def logger():
    """Fixture que retorna a instância do logger configurado."""
    # Retorna o logger configurado no início do arquivo
    # return logging.getLogger(__name__) # Pode usar o logger do módulo de teste
    return api_logger  # Ou retorna o logger específico criado acima


# --- Configuração do Pytest (para encontrar testes) ---
# Geralmente, o pytest descobre os testes automaticamente se a estrutura
# e a nomeação (test_*.py ou *_test.py) estiverem corretas.
# Esta seção pode ser necessária em cenários mais complexos de importação,
# mas para esta estrutura, o pytest deve funcionar sem adições aqui
# se executado a partir do diretório raiz (project_root).

# Exemplo de como adicionar o diretório raiz ao sys.path se necessário:
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
