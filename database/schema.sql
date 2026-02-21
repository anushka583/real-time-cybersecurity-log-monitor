CREATE DATABASE IF NOT EXISTS cyber_logs;
USE cyber_logs;
CREATE TABLE IF NOT EXISTS security_logs
(
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    timestamp DATETIME NOT NULL,
    source_ip VARCHAR(45) NOT NULL,
    destination_ip VARCHAR(45) NOT NULL,
    country VARCHAR(50),
    event_type VARCHAR(50),
    status VARCHAR(20),
    response_time_ms INT
);

CREATE INDEX idx_timestamp ON security_logs(timestamp);
CREATE INDEX idx_source_ip ON security_logs(source_ip);
CREATE INDEX idx_event_type ON security_logs(event_type);
CREATE INDEX idx_status ON security_logs(status);