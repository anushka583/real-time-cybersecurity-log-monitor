print("Step 1: File started")
from db_config import get_connection
print("Step 2: Import successful")
try:
    print("Step 3: Attempting connection...")
    conn=get_connection()
    print("Step 4: Connection successful")
    conn.close()
    print("Step 5: Connection closed")
except Exception as e:
    print("Error!")
    print(e)