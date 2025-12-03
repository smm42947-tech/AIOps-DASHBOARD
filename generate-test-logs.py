#!/usr/bin/env python3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Create massive log file with patterns
def generate_anomaly_logs(num_records=1000):
    services = [
        'web-server', 'database', 'auth-service', 'api-gateway', 
        'cache', 'load-balancer', 'payment-service', 'order-service',
        'user-service', 'notification-service', 'inventory-service',
        'firewall', 'ids', 'waf', 'monitoring-service'
    ]
    
    log_levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL', 'DEBUG']
    # Adjusted probabilities for more anomalies
    level_probs = [0.4, 0.25, 0.2, 0.1, 0.05]
    
    messages = {
        'INFO': [
            'User login successful',
            'Request processed successfully',
            'Database connection established',
            'Cache hit',
            'Email sent successfully',
            'Health check passed',
            'Backup completed',
            'Data synchronized',
            'Service started',
            'Configuration loaded'
        ],
        'WARNING': [
            'High response time detected',
            'Memory usage above threshold',
            'Disk space low',
            'CPU temperature high',
            'Network latency increased',
            'Slow query detected',
            'Cache miss rate high',
            'Connection pool at 80%',
            'SSL certificate expiring soon',
            'Unusual traffic pattern'
        ],
        'ERROR': [
            'Authentication failed',
            'Database connection lost',
            'Payment processing failed',
            'Service timeout',
            'File not found',
            'Permission denied',
            'Network unreachable',
            'Out of memory',
            'Disk write failed',
            'API rate limit exceeded'
        ],
        'CRITICAL': [
            'System crash imminent',
            'Data corruption detected',
            'Security breach',
            'Service outage',
            'Hardware failure',
            'Data loss detected',
            'Complete system failure',
            'Recovery impossible',
            'Critical vulnerability',
            'Emergency shutdown required'
        ],
        'DEBUG': [
            'Processing request ID 12345',
            'Cache key: user_profile_789',
            'SQL query executed',
            'API call to external service',
            'Parsing JSON response',
            'Validating user input',
            'Generating JWT token',
            'Compressing response',
            'Logging metric data',
            'Cleaning temporary files'
        ]
    }
    
    logs = []
    base_time = datetime.now() - timedelta(hours=2)
    
    # Create anomaly patterns
    anomaly_periods = [
        (30, 40),   # First anomaly period
        (80, 90),   # Second anomaly period
        (150, 160), # Third anomaly period
        (220, 230), # Fourth anomaly period
        (300, 310)  # Fifth anomaly period
    ]
    
    for i in range(num_records):
        # Time with some randomness
        timestamp = base_time + timedelta(seconds=i*2 + random.randint(0, 5))
        
        # Check if this is an anomaly period
        is_anomaly = False
        for start, end in anomaly_periods:
            if start <= i <= end:
                is_anomaly = True
                break
        
        if is_anomaly:
            # During anomaly, increase ERROR and CRITICAL probabilities
            anomaly_probs = [0.2, 0.2, 0.3, 0.25, 0.05]
            level = np.random.choice(log_levels, p=anomaly_probs)
            service = 'system' if random.random() < 0.7 else random.choice(services)
            
            # Special anomaly messages
            if level in ['ERROR', 'CRITICAL']:
                anomaly_msgs = [
                    f'CPU spike to {random.randint(85, 99)}%',
                    f'Memory leak detected - usage at {random.randint(90, 99)}%',
                    f'Disk I/O bottleneck - latency {random.randint(500, 2000)}ms',
                    f'Network packet loss {random.randint(10, 30)}%',
                    f'Service response time degraded to {random.randint(2000, 5000)}ms',
                    f'Database deadlock detected',
                    f'Cache cluster failure',
                    f'Load balancer overwhelmed',
                    f'API gateway timeout cascade',
                    f'Distributed system partition'
                ]
                message = random.choice(anomaly_msgs)
            else:
                message = random.choice(messages[level])
        else:
            # Normal operation
            level = np.random.choice(log_levels, p=level_probs)
            service = random.choice(services)
            message = random.choice(messages[level])
        
        # Add correlation ID for related logs
        correlation_id = f'corr_{random.randint(1000, 9999)}' if random.random() < 0.3 else ''
        
        logs.append({
            'timestamp': timestamp,
            'level': level,
            'service': service,
            'message': message,
            'source_ip': f'10.0.{random.randint(0, 255)}.{random.randint(1, 254)}',
            'response_time_ms': random.randint(10, 5000) if level in ['ERROR', 'WARNING'] else random.randint(10, 500),
            'correlation_id': correlation_id,
            'is_anomaly': 1 if is_anomaly else 0
        })
    
    return pd.DataFrame(logs)

# Generate and save logs
print("Generating test logs with anomalies...")
df = generate_anomaly_logs(1000)

# Save to CSV
csv_file = 'anomaly-test-logs.csv'
df.to_csv(csv_file, index=False)
print(f"Generated {len(df)} log entries")
print(f"Saved to: {csv_file}")

# Show statistics
print("\n📊 Log Statistics:")
print(f"Total logs: {len(df)}")
print(f"INFO: {len(df[df['level'] == 'INFO'])}")
print(f"WARNING: {len(df[df['level'] == 'WARNING'])}")
print(f"ERROR: {len(df[df['level'] == 'ERROR'])}")
print(f"CRITICAL: {len(df[df['level'] == 'CRITICAL'])}")
print(f"DEBUG: {len(df[df['level'] == 'DEBUG'])}")
print(f"Anomalies: {len(df[df['is_anomaly'] == 1])}")

# Create a summary file
summary = f"""
=== AIOps Test Logs Summary ===
Generated: {datetime.now()}
Total Records: {len(df)}
Time Range: {df['timestamp'].min()} to {df['timestamp'].max()}
Anomaly Periods: 5 clusters
Services: {df['service'].nunique()} unique services
Correlation IDs: {df['correlation_id'].nunique() - 1} unique correlations

Anomaly Pattern:
- Period 1: Records 30-40 (System stress)
- Period 2: Records 80-90 (Memory leak)
- Period 3: Records 150-160 (Network issues)
- Period 4: Records 220-230 (Database problems)
- Period 5: Records 300-310 (Cascade failure)

Use these logs to test:
1. Anomaly detection in dashboard
2. Log filtering and searching
3. Correlation analysis
4. Pattern recognition
"""
print(summary)

with open('logs-summary.txt', 'w') as f:
    f.write(summary)
