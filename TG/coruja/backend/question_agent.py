from typing import List, Dict, Any, Optional, Tuple
import json
from ollama import AsyncClient
import os
import psycopg2

class QuestionAgent:
    def __init__(self, ollama_client: AsyncClient):
        self.ollama_client = ollama_client
        self.context = []
        self.current_question = None
        
    def process_response(self, user_response: str) -> str:
        """
        Process the user's response and generate feedback.
        
        Args:
            user_response (str): The user's answer to the question
            
        Returns:
            str: Feedback for the user's response
        """
        try:
            # Get response from the language model synchronously
            response = self.ollama_client.chat(
                model="mistral",
                messages=[{
                    "role": "user", 
                    "content": f"Avalie a seguinte resposta do estudante: {user_response}"
                }]
            )
            
            # Generate simple feedback
            feedback = "Resposta registrada com sucesso! Continue assim!"
            
            # Update the next question
            self.current_question = "Qual é a sua opinião sobre o tema discutido?"
            
            return feedback
            
        except Exception as e:
            return f"Erro ao processar resposta: {str(e)}"
            
    def _validate_feedback_format(self, feedback: Dict[str, Any]) -> bool:
        """
        Validate that the feedback dictionary has all required fields.
        
        Args:
            feedback (Dict[str, Any]): The feedback dictionary to validate
            
        Returns:
            bool: True if the feedback has all required fields, False otherwise
        """
        required_fields = {
            "avaliacao": ["esta_correto", "explicacao", "sugestoes"],
            "proxima_pergunta": ["texto", "contexto"]
        }
        
        try:
            for section, fields in required_fields.items():
                if section not in feedback:
                    return False
                for field in fields:
                    if field not in feedback[section]:
                        return False
            return True
        except Exception:
            return False
            
    def update_context(self, question: str, response: str, feedback: Dict[str, Any]):
        """
        Update the conversation context with the latest interaction.
        
        Args:
            question (str): The question that was asked
            response (str): The user's response
            feedback (Dict[str, Any]): The feedback provided by the model
        """
        self.context.append({
            "question": question,
            "response": response,
            "feedback": feedback
        })
        self.current_question = feedback["proxima_pergunta"]["texto"]
        
    def get_current_question(self) -> Optional[str]:
        """
        Get the current question in the conversation.
        
        Returns:
            Optional[str]: The current question or None if no question is set
        """
        return self.current_question
        
    def update_current_question(self, question):
        """Atualiza a pergunta atual da sessão."""
        self.current_question = question 