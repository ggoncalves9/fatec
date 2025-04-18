import psycopg2
import random
import os
import time

# Delay simples para garantir que o banco esteja pronto
time.sleep(10)

def get_daily_questions(tema='Linux', dificuldade='EASY'):
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT", 5432)
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT pergunta FROM cad_questoes
        WHERE tema_estudo = %s AND dificuldade = %s
    """, (tema, dificuldade))

    questoes = cur.fetchall()
    cur.close()
    conn.close()

    perguntas = random.sample(questoes, min(5, len(questoes)))
    return [q[0] for q in perguntas]

if __name__ == "__main__":
    perguntas = get_daily_questions(tema='Linux', dificuldade='EASY')
    print("📘 Missão do Dia: Responder essas perguntas!\n")
    for i, p in enumerate(perguntas, 1):
        print(f"{i}. {p}")
