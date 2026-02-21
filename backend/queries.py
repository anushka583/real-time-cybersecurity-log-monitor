from db_config import get_connection

def get_total_logs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM security_logs")
    result = cursor.fetchone()[0]
    conn.close()
    return result


def get_failed_logins():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM security_logs WHERE status='FAILED'")
    result = cursor.fetchone()[0]
    conn.close()
    return result


def get_top_attacking_ips(limit=5):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT source_ip, COUNT(*) as attempts
    FROM security_logs
    GROUP BY source_ip
    ORDER BY attempts DESC
    LIMIT %s
    """
    cursor.execute(query, (limit,))
    results = cursor.fetchall()
    conn.close()
    return results


def get_events_over_time():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT DATE(timestamp), COUNT(*)
    FROM security_logs
    GROUP BY DATE(timestamp)
    ORDER BY DATE(timestamp)
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results



def detect_brute_force(threshold=5, time_window_minutes=5):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT source_ip, COUNT(*) as attempts 
    FROM security_logs
    WHERE status='FAILED'
    AND timestamp >= NOW() - INTERVAL %s MINUTE
    GROUP BY source_ip
    HAVING attempts >= %s
    """

    cursor.execute(query, (time_window_minutes, threshold))
    results = cursor.fetchall()

    conn.close()
    return results  