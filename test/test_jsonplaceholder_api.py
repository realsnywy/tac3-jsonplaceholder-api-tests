import requests
import pytest
import logging  # Importa logging para usar o logger

# Nota: A fixture 'logger' é injetada automaticamente pelo pytest
# devido à sua definição em conftest.py

# --- Testes para JSONPlaceholder API ---


@pytest.mark.usefixtures("logger", "base_url")  # Declara o uso das fixtures
class TestJSONPlaceholderAPI:
    """Grupo de testes para as operações CRUD da JSONPlaceholder API."""

    # --- Testes de Consulta (READ) ---

    def test_get_all_posts(self, logger, base_url):
        """Verifica a consulta de todos os posts."""
        logger.info("Iniciando test_get_all_posts")
        url = f"{base_url}/posts"
        logger.info(f"Enviando GET para {url}")
        response = requests.get(url)
        logger.info(f"Recebido status code: {response.status_code}")

        assert (
            response.status_code == 200
        ), f"Esperado status code 200, mas foi {response.status_code}"
        posts = response.json()
        assert isinstance(posts, list), "A resposta deveria ser uma lista de posts"
        assert len(posts) > 0, "A lista de posts não deveria estar vazia"
        logger.info(f"Recebidos {len(posts)} posts. Teste concluído com sucesso.")

    def test_get_specific_post(self, logger, base_url):
        """Verifica a consulta de um post específico pelo ID."""
        post_id = 1
        logger.info(f"Iniciando test_get_specific_post para o post ID: {post_id}")
        url = f"{base_url}/posts/{post_id}"
        logger.info(f"Enviando GET para {url}")
        response = requests.get(url)
        logger.info(f"Recebido status code: {response.status_code}")

        assert (
            response.status_code == 200
        ), f"Esperado status code 200, mas foi {response.status_code}"
        post = response.json()
        assert isinstance(
            post, dict
        ), "A resposta deveria ser um dicionário representando o post"
        assert (
            post.get("id") == post_id
        ), f"O ID do post na resposta ({post.get('id')}) não corresponde ao ID solicitado ({post_id})"
        logger.info(f"Post ID {post_id} recuperado com sucesso. Teste concluído.")

    def test_get_comments_for_post(self, logger, base_url):
        """Verifica a consulta de comentários relacionados a um post específico."""
        post_id = 1
        logger.info(f"Iniciando test_get_comments_for_post para o post ID: {post_id}")
        url = f"{base_url}/posts/{post_id}/comments"
        # Alternativa: url = f"{base_url}/comments?postId={post_id}"
        logger.info(f"Enviando GET para {url}")
        response = requests.get(url)
        logger.info(f"Recebido status code: {response.status_code}")

        assert (
            response.status_code == 200
        ), f"Esperado status code 200, mas foi {response.status_code}"
        comments = response.json()
        assert isinstance(
            comments, list
        ), "A resposta deveria ser uma lista de comentários"
        assert (
            len(comments) > 0
        ), f"Esperava-se comentários para o post ID {post_id}, mas a lista está vazia"
        # Verifica se todos os comentários retornados pertencem ao post correto
        for comment in comments:
            assert (
                comment.get("postId") == post_id
            ), f"Comentário ID {comment.get('id')} tem postId {comment.get('postId')}, esperado {post_id}"
        logger.info(
            f"Comentários para o post ID {post_id} recuperados com sucesso. Teste concluído."
        )

    # --- Testes de Criação (CREATE) ---

    def test_create_post(self, logger, base_url):
        """Verifica a criação de um novo post."""
        logger.info("Iniciando test_create_post")
        url = f"{base_url}/posts"
        new_post_data = {
            "title": "Meu Novo Post de Teste",
            "body": "Este é o conteúdo do post criado pelo teste automatizado.",
            "userId": 101,  # Usando um userId fictício
        }
        logger.info(f"Enviando POST para {url} com dados: {new_post_data}")
        response = requests.post(url, json=new_post_data)
        logger.info(f"Recebido status code: {response.status_code}")

        # JSONPlaceholder retorna 201 Created
        assert (
            response.status_code == 201
        ), f"Esperado status code 201, mas foi {response.status_code}"
        created_post = response.json()
        logger.info(f"Post criado: {created_post}")
        assert isinstance(created_post, dict), "A resposta deveria ser um dicionário"
        # JSONPlaceholder retorna um ID para o novo post (geralmente > 100)
        assert (
            "id" in created_post
        ), "A resposta deveria conter um 'id' para o novo post"
        assert (
            created_post.get("title") == new_post_data["title"]
        ), "O título do post criado não corresponde ao enviado"
        assert (
            created_post.get("body") == new_post_data["body"]
        ), "O corpo do post criado não corresponde ao enviado"
        assert (
            created_post.get("userId") == new_post_data["userId"]
        ), "O userId do post criado não corresponde ao enviado"
        logger.info(
            f"Novo post criado com ID {created_post.get('id')}. Teste concluído com sucesso."
        )

    # --- Testes de Atualização (UPDATE) ---

    def test_update_post_put(self, logger, base_url):
        """Verifica a atualização completa de um post existente (PUT)."""
        post_id = 1
        logger.info(f"Iniciando test_update_post_put para o post ID: {post_id}")
        url = f"{base_url}/posts/{post_id}"
        updated_post_data = {
            "id": post_id,  # PUT geralmente requer o ID no corpo também
            "title": "Post Atualizado Totalmente",
            "body": "Conteúdo completamente modificado pelo método PUT.",
            "userId": 1,
        }
        logger.info(f"Enviando PUT para {url} com dados: {updated_post_data}")
        response = requests.put(url, json=updated_post_data)
        logger.info(f"Recebido status code: {response.status_code}")

        assert (
            response.status_code == 200
        ), f"Esperado status code 200, mas foi {response.status_code}"
        updated_post = response.json()
        logger.info(f"Post atualizado (PUT): {updated_post}")
        assert isinstance(updated_post, dict), "A resposta deveria ser um dicionário"
        assert (
            updated_post.get("id") == post_id
        ), "O ID do post atualizado não corresponde"
        assert (
            updated_post.get("title") == updated_post_data["title"]
        ), "O título não foi atualizado corretamente"
        assert (
            updated_post.get("body") == updated_post_data["body"]
        ), "O corpo não foi atualizado corretamente"
        assert (
            updated_post.get("userId") == updated_post_data["userId"]
        ), "O userId não foi atualizado corretamente"
        logger.info(
            f"Post ID {post_id} atualizado via PUT com sucesso. Teste concluído."
        )

    def test_update_post_patch(self, logger, base_url):
        """Verifica a atualização parcial de um post existente (PATCH)."""
        post_id = 1
        logger.info(f"Iniciando test_update_post_patch para o post ID: {post_id}")
        url = f"{base_url}/posts/{post_id}"
        partial_update_data = {"title": "Post Atualizado Parcialmente (PATCH)"}
        logger.info(f"Enviando PATCH para {url} com dados: {partial_update_data}")
        response = requests.patch(url, json=partial_update_data)
        logger.info(f"Recebido status code: {response.status_code}")

        assert (
            response.status_code == 200
        ), f"Esperado status code 200, mas foi {response.status_code}"
        updated_post = response.json()
        logger.info(f"Post atualizado (PATCH): {updated_post}")
        assert isinstance(updated_post, dict), "A resposta deveria ser um dicionário"
        assert (
            updated_post.get("id") == post_id
        ), "O ID do post atualizado não corresponde"
        assert (
            updated_post.get("title") == partial_update_data["title"]
        ), "O título não foi atualizado corretamente via PATCH"
        # Outros campos (body, userId) devem permanecer inalterados (JSONPlaceholder pode retornar o objeto completo)
        assert (
            "body" in updated_post
        ), "O corpo do post deveria estar presente na resposta"
        assert (
            "userId" in updated_post
        ), "O userId do post deveria estar presente na resposta"
        logger.info(
            f"Post ID {post_id} atualizado via PATCH com sucesso. Teste concluído."
        )

    # --- Testes de Exclusão (DELETE) ---

    def test_delete_post(self, logger, base_url):
        """Verifica a exclusão de um post existente."""
        post_id = 1
        logger.info(f"Iniciando test_delete_post para o post ID: {post_id}")
        url = f"{base_url}/posts/{post_id}"
        logger.info(f"Enviando DELETE para {url}")
        response = requests.delete(url)
        logger.info(f"Recebido status code: {response.status_code}")

        # JSONPlaceholder retorna 200 OK para DELETE, não 204 No Content
        assert (
            response.status_code == 200
        ), f"Esperado status code 200 para DELETE, mas foi {response.status_code}"
        # A resposta de DELETE na JSONPlaceholder é um corpo vazio {}
        assert (
            response.json() == {}
        ), "A resposta do DELETE deveria ser um JSON vazio {}"

        # Opcional: Tentar buscar o post deletado para confirmar (deve retornar 404)
        logger.info(
            f"Verificando se o post ID {post_id} foi realmente deletado (esperado 404)"
        )
        verify_response = requests.get(url)
        logger.info(
            f"Status code da verificação GET após DELETE: {verify_response.status_code}"
        )
        # ATENÇÃO: JSONPlaceholder é uma API fake. Ela não persiste o estado de DELETE.
        # Portanto, a verificação abaixo FALHARÁ com JSONPlaceholder, pois o GET ainda retornará 200.
        # Em uma API real, esperaríamos 404 aqui.
        # assert verify_response.status_code == 404, f"Esperado 404 ao buscar post deletado, mas foi {verify_response.status_code}"
        logger.warning(
            f"JSONPlaceholder não persiste DELETEs, a verificação de 404 após DELETE não é aplicável aqui."
        )
        logger.info(
            f"DELETE para post ID {post_id} processado (status {response.status_code}). Teste concluído."
        )

    # --- Testes de Tratamento de Erros ---

    def test_get_non_existent_post(self, logger, base_url):
        """Verifica o comportamento da API ao solicitar um recurso inexistente."""
        non_existent_post_id = 9999
        logger.info(
            f"Iniciando test_get_non_existent_post para o post ID: {non_existent_post_id}"
        )
        url = f"{base_url}/posts/{non_existent_post_id}"
        logger.info(f"Enviando GET para {url}")
        response = requests.get(url)
        logger.info(f"Recebido status code: {response.status_code}")

        # APIs RESTful tipicamente retornam 404 Not Found para recursos inexistentes
        assert (
            response.status_code == 404
        ), f"Esperado status code 404 para recurso inexistente, mas foi {response.status_code}"
        logger.info(
            f"Recebido 404 esperado para post inexistente ID {non_existent_post_id}. Teste concluído com sucesso."
        )
