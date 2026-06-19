import time
import os
import requests

log_file = "system_integrity.log"
N8N_URL = "https://assistant01tulsi.app.n8n.cloud/webhook-test/ransomware-alert"

while not os.path.exists(log_file):
    time.sleep(0.1)

file = open(log_file, "r")
file.seek(0, os.SEEK_END)

print("Integrity Scanning Engine Engaged. Standing guard...")

while True:
    line = file.readline()
    if not line:
        time.sleep(0.1)
        continue
        
    clean_line = line.strip()
    
    # Check for the malware signature string footprint
    if "ENCRYPT_AES_256" in clean_line:
        print("\n💥 RANSOMWARE ENCRYPTION SIGNATURE IDENTIFIED!")
        print(f"FOOTPRINT DATA: {clean_line}\n")
        
        # Structure the incident report dictionary
        incident_report = {
            "threat_actor": "Ransomware_Mutex_Variant_A",
            "malware_signature": "ENCRYPT_AES_256",
            "compromised_log": clean_line
        }
        
        # Dispatch the malicious footprint over the API layer to n8n
        try:
            res = requests.post(N8N_URL, json=incident_report)
            print(f"[SOAR LINK] Incident dispatch successful. Gateway code: {res.status_code}")
        except Exception as e:
            print(f"Gateway link block: {e}")