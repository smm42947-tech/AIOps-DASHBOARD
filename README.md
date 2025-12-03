# 🚀 AIOps Dashboard - System Monitoring & Analytics

![AIOps Dashboard](https://img.shields.io/badge/AIOps-Dashboard-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-green?logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Deployed-0089D6?logo=microsoft-azure&logoColor=white)

A comprehensive AIOps (Artificial Intelligence for IT Operations) dashboard for real-time system monitoring, log analysis, and anomaly detection deployed on Azure Ubuntu VM.

## ✨ Live Demo
**Access Dashboard:** `http://<your-vm-ip>:8501`

## 📋 Features

### 📊 **System Health Monitoring**
- Real-time CPU, RAM, Disk usage monitoring
- Network I/O statistics visualization
- Threshold-based alert system
- System status indicators

### 📈 **Metrics Visualization**
- Interactive Plotly charts (CPU, RAM, Disk I/O)
- 60-minute historical data window
- Configurable alert thresholds
- Real-time metrics dashboard

### 📄 **Log Explorer & Analysis**
- Upload log files (.log, .txt, .csv)
- Advanced filtering by level, service, time
- Search within log messages
- Export filtered logs to CSV
- Log statistics and visualizations

### 🔍 **Anomaly Detection**
- ML-based anomaly detection (Isolation Forest)
- Automatic correlation with logs
- Adjustable sensitivity controls
- Real-time anomaly simulation
- Pattern recognition

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "🖥️ User Interface Layer"
        UI[AIOps Dashboard UI]
        T1[📊 Quick Overview]
        T2[📈 Metrics Monitor]
        T3[📄 Log Explorer]
        T4[🔍 Anomaly Detection]
        UI --> T1
        UI --> T2
        UI --> T3
        UI --> T4
    end
    
    subgraph "🔧 Processing Layer"
        subgraph "Data Collection"
            DC1[psutil - System Metrics]
            DC2[Real-time Monitoring]
            DC3[Network I/O Stats]
        end
        
        subgraph "Analysis Engine"
            AE1[Log Parsing]
            AE2[Filtering & Search]
            AE3[Correlation Engine]
        end
        
        subgraph "ML Engine"
            ML1[Isolation Forest]
            ML2[Anomaly Detection]
            ML3[Pattern Recognition]
        end
    end
    
    subgraph "💾 Data Layer"
        IM[In-memory Storage]
        FS[File System Storage]
        VD[Visualization Data]
    end
    
    subgraph "🌐 Infrastructure Layer"
        VM[Azure Ubuntu VM<br/>B2s - 2vCPU, 4GB RAM]
        PY[Python 3.12 Environment]
        WS[Streamlit Server<br/>Port 8501]
        SEC[Security & Networking<br/>Azure NSG, UFW, Systemd]
    end
    
    User[👤 End User] -->|HTTP Request| UI
    UI -->|Dashboard Updates| User
    
    UI --> DC1
    UI --> AE1
    UI --> ML1
    
    DC1 -->|Real-time Metrics| IM
    AE1 -->|Processed Logs| FS
    ML1 -->|Anomaly Scores| VD
    
    IM -->|Visualization Data| T1
    FS -->|Filtered Logs| T3
    VD -->|Detection Results| T4
    
    VM --> PY
    PY --> WS
    WS --> UI
    SEC --> VM
    
    style UI fill:#e1f5fe
    style T1 fill:#bbdefb
    style T2 fill:#bbdefb
    style T3 fill:#bbdefb
    style T4 fill:#bbdefb
    style DC1 fill:#c8e6c9
    style AE1 fill:#fff9c4
    style ML1 fill:#ffccbc
    style IM fill:#f3e5f5
    style VM fill:#fce4ec

🚀 Quick Start
Prerequisites
Azure Ubuntu VM (or any Linux server)

Python 3.8+
