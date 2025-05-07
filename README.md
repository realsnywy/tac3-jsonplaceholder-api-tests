# Projeto de Testes Automatizados para API - JSONPlaceholder

Este projeto implementa testes automatizados para a API REST pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/) utilizando Python, `pytest` e `requests`.

## Estrutura do Projeto

```
project_root/
├── app/                 # Contém configurações, runner e dependências
│   ├── __init__.py      # Marca como pacote Python
│   ├── conftest.py      # Configurações e fixtures do pytest (logging, base_url)
│   ├── requirements.txt # Lista de dependências Python
│   └── run_tests.py     # Script para executar os testes
├── test/                # Contém os arquivos de teste
│   ├── __init__.py      # Marca como pacote Python
│   └── test_jsonplaceholder_api.py # Testes para a API JSONPlaceholder
└── README.md            # Este arquivo
```

## Configuração do Ambiente

1. **Clone o Repositório:**

    ```bash
    git clone <url-do-seu-repositorio>
    cd project_root
    ```

2. **Crie um Ambiente Virtual (Recomendado):**

    ```bash
    python -m venv venv
    ```

    *No Windows:*

    ```bash
    venv\Scripts\activate
    ```

    *No macOS/Linux:*

    ```bash
    source venv/bin/activate
    ```

3. **Instale as Dependências:**
    Navegue até o diretório `project_root` (se ainda não estiver lá) e execute:

    ```bash
    pip install -r app/requirements.txt
    ```

## Executando os Testes

Existem duas formas principais de executar os testes:

1. **Usando o Script `run_tests.py`:**
    Execute o script a partir do diretório `project_root`:

    ```bash
    python app/run_tests.py
    ```

    Este script chamará o `pytest` com configurações básicas (modo verbose).

2. **Usando o Comando `pytest` Diretamente:**
    Execute o comando `pytest` a partir do diretório `project_root`:

    ```bash
    pytest
    ```

    Você pode adicionar flags para mais detalhes ou funcionalidades:

    ```bash
    pytest -v                # Modo verbose
    pytest -s                # Mostra output (útil para ver prints e logs no console)
    pytest test/test_jsonplaceholder_api.py::TestJSONPlaceholderAPI::test_create_post # Executa um teste específico
    pytest -k "create or update" # Executa testes cujo nome contém "create" ou "update"
    ```

## Logging

Os testes utilizam o módulo `logging` do Python para registrar informações sobre a execução. Por padrão, os logs são exibidos no console durante a execução dos testes. A configuração do logging está em `app/conftest.py`. Você pode descomentar as linhas relevantes em `app/conftest.py` para direcionar os logs para um arquivo (`logs/test_run.log`).

## Cobertura dos Testes

O arquivo `test/test_jsonplaceholder_api.py` inclui testes para:

* **READ:** Consultar todos os posts, um post específico e comentários de um post.
* **CREATE:** Criar um novo post.
* **UPDATE:** Atualizar um post existente usando PUT (completo) e PATCH (parcial).
* **DELETE:** Excluir um post existente.
* **Error Handling:** Tentar consultar um post inexistente (esperando 404).

*Observação sobre DELETE:* A JSONPlaceholder é uma API simulada e não persiste o estado das operações de escrita (POST, PUT, PATCH, DELETE) entre chamadas. Portanto, a verificação pós-DELETE (tentar buscar o recurso excluído e esperar 404) não funciona como em uma API real. O teste de DELETE verifica apenas se a API retorna o status code esperado (200) para a operação DELETE.
