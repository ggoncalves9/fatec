import requests
import psycopg2
import httpx
import asyncio
from datetime import datetime

def test_postgres():
    try:
        conn = psycopg2.connect(
            host="192.168.15.161",
            port="5432",
            database="coruja_db",
            user="coruja_user",
            password="coruja_pass"
        )
        conn.close()
        return True, "Conexão com PostgreSQL bem-sucedida"
    except Exception as e:
        return False, f"Erro ao conectar com PostgreSQL: {str(e)}"

def test_backend():
    try:
        response = requests.get("http://192.168.15.161:5000/")
        return True, f"Conexão com Backend bem-sucedida. Status: {response.status_code}"
    except Exception as e:
        return False, f"Erro ao conectar com Backend: {str(e)}"

def test_ui():
    try:
        response = requests.get("http://192.168.15.161:8080/")
        return True, f"Conexão com UI bem-sucedida. Status: {response.status_code}"
    except Exception as e:
        return False, f"Erro ao conectar com UI: {str(e)}"

async def test_ollama():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://192.168.15.161:11434/api/tags")
            return True, f"Conexão com Ollama bem-sucedida. Status: {response.status_code}"
    except Exception as e:
        return False, f"Erro ao conectar com Ollama: {str(e)}"

async def main():
    print(f"\nTeste de Conexão - {datetime.now()}")
    print("=" * 50)
    
    # Teste PostgreSQL
    success, message = test_postgres()
    print(f"\nPostgreSQL: {'✅' if success else '❌'} {message}")
    
    # Teste Backend
    success, message = test_backend()
    print(f"\nBackend: {'✅' if success else '❌'} {message}")
    
    # Teste UI
    success, message = test_ui()
    print(f"\nUI: {'✅' if success else '❌'} {message}")
    
    # Teste Ollama
    success, message = await test_ollama()
    print(f"\nOllama: {'✅' if success else '❌'} {message}")

if __name__ == "__main__":
    asyncio.run(main()) 