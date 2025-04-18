import httpx
import os
from typing import List, Dict, Any

class OllamaClient:
    def __init__(self):
        self.base_url = f"http://{os.environ.get('OLLAMA_HOST', 'localhost')}:{os.environ.get('OLLAMA_PORT', '11434')}"
        self.client = httpx.AsyncClient(timeout=30.0)

    async def generate_response(self, model: str, prompt: str) -> str:
        """Gera uma resposta usando o modelo especificado."""
        try:
            response = await self.client.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            print(f"Erro ao gerar resposta: {str(e)}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação."

    async def chat(self, model: str, messages: List[Dict[str, str]]) -> str:
        """Realiza um chat com o modelo especificado."""
        try:
            response = await self.client.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["message"]["content"]
        except Exception as e:
            print(f"Erro no chat: {str(e)}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação."

    async def list_models(self) -> List[str]:
        """Lista os modelos disponíveis no Ollama."""
        try:
            response = await self.client.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            return [model["name"] for model in response.json()["models"]]
        except Exception as e:
            print(f"Erro ao listar modelos: {str(e)}")
            return []

    async def pull_model(self, model: str) -> bool:
        """Baixa um modelo específico do Ollama."""
        try:
            response = await self.client.post(
                f"{self.base_url}/api/pull",
                json={"name": model}
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Erro ao baixar modelo: {str(e)}")
            return False

    async def close(self):
        """Fecha a conexão com o cliente."""
        await self.client.aclose() 