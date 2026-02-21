import random
import time
from datetime import datetime
from faker import Faker
from db_config import get_connection
fake=Faker()
EVENT_TYPES=["LOGIN","FILE_ACCESS","DATA_EXPORT","PASSWORD_CHANGE"]
STATUS_TYPES=["SUCCESS","FAILED"]

def generate_log():
    conn=get_connection()
    cursor=conn.cursor()
    query="""
    INSERT INTO security_logs
    (timestamp,source_ip,destination_ip,country,event_type,status,response_time_ms)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """
    values=(
        datetime.now(),
        fake.ipv4(),
        fake.ipv4(),
        fake.country(),
        random.choice(EVENT_TYPES),
        random.choice(STATUS_TYPES),
        random.randint(10,2000)
    )
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Log inserted:",values)
if __name__=="__main__":
    print("Starting log generator...")
    while True:
        generate_log()
        time.sleep(2)