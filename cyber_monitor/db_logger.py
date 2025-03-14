import psycopg2
from datetime import datetime

DB_NAME = "security_logs"
DB_USER = "admin"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"

def log_threat(event, risk_level):
    """
    Anormal trafik aşkar edildikdə, bunu PostgreSQL bazasına yazır.
    """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cur.execute(
            "INSERT INTO logs (event, risk_level, timestamp) VALUES (%s, %s, %s)",
            (event, risk_level, timestamp),
        )
        
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Threat logged in database.")
    
    except Exception as e:
        print(f"❌ Database logging failed: {e}")
