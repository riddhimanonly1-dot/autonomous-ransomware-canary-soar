import time
import os
import random
from datetime import datetime

watch_directory = "critical_assets"
log_file_path = "system_integrity.log"

# Create a fake sensitive directory if it doesn't exist
if not os.path.exists(watch_directory):
    os.makedirs(watch_directory)
    # Generate a fake database file inside the trap folder
    with open(f"{watch_directory}/grid_db.conf", "w") as f:
        f.write("DATABASE_ENCRYPTION_KEY_PLAINTEXT=SAFE_KEY_XYZ_123")

print(f"Monitoring folder [{watch_directory}] for Ransomware File Traps...")

# Infinite tracker loop (Like while(true) in Java)
while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Simulate an external malware attack event randomly (10% chance)
    exploit_trigger = random.randint(0, 10)
    
    with open(log_file_path, "a") as log:
        if exploit_trigger == 7:
            # Simulate a ransomware payload modifying the database format extension
            attack_entry = f"[{current_time}] CRITICAL | PAYLOAD: ENCRYPT_AES_256 | TARGET: grid_db.conf.locked | TRACE: RANSOM_MUTEX_0x4F\n"
            print("🚨 SECURITY VIOLATION: Ransomware file modification signature caught!")
            log.write(attack_entry)
        else:
            # Log normal background system processes
            normal_entry = f"[{current_time}] VERIFY | PROCESS: SYSTEM_DAEMON | TARGET: grid_db.conf | STATUS: UNMODIFIED\n"
            log.write(normal_entry)
            
    time.sleep(0.1)