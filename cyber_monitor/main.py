from packet_sniffer import start_sniffing
from anomaly_detector import is_anomalous
from alert_system import send_email_alert, send_telegram_alert
from db_logger import log_threat

def packet_callback(packet):
    packet_data = [0.2, 0.7, 0.8, 0.1, 0.5]  # Burada real paket məlumatları olmalıdır

    if is_anomalous(packet_data):
        print("⚠️ Warning: Anomaly detected!")
        send_email_alert("🚨 Possible cyber threat detected!")
        send_telegram_alert("🚨 Possible cyber threat detected!")
        log_threat("Unknown Attack", "Medium")

if __name__ == "__main__":
    print("Cyber Security Monitor Starting...")
    start_sniffing()
