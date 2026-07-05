from sqlalchemy import text
from sqlalchemy import create_engine
import time
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

engine = create_engine(DATABASE_URI)

def sim_n_plus_one():
    print("This one simulates n+1 queries")
    start_time = time.time()
    q_count = 0

    with engine.connect() as conn:
        enrollments = conn.execute(text("SELECT * FROM enrollments")).fetchall()
        q_count+=1
        

        for enrollment in enrollments:
            student_id = enrollment.student_id
            student = conn.execute(text(f"SELECT first_name, last_name FROM students WHERE student_id = {student_id}")).fetchone()
            q_count += 1
    
    end_time = time.time()

    print(f"Total time : {end_time - start_time:.4f} seconds")
    print(f"Total queries : {q_count}")

def optimized_join():
    print("This one runs optimized JOINs")
    start_time = time.time()
    query_count = 0
    
    with engine.connect() as conn:
        query = """
            SELECT e.*, s.first_name, s.last_name 
            FROM enrollments e 
            JOIN students s ON e.student_id = s.student_id
        """
        results = conn.execute(text(query)).fetchall()
        query_count += 1
        
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.4f} seconds")
    print(f"{query_count} query executed\n")

if __name__ == "__main__":
    sim_n_plus_one()
    optimized_join()

# OUTPUT:
# This one simulates n+1 queries
# Total time : 0.0517 seconds
# Total queries : 18
# This one runs optimized JOINs
# Total time: 0.0009 seconds
# 1 query executed

#  in a real application with 10,000 enrollments, how many extra queries would the N+1 version issue

# N+1 Approach: 1 query (to fetch 10,000 enrollments) + 10,000 queries (inside the loop) = 10,001 total queries.
# JOIN Approach: 1 total query.
# Extra queries issued: 10,000.

