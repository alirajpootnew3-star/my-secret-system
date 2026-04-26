import os
import random

def rotate():
    # Aapke 4 VIP names
    prefixes = ["ILYAS_KH_YT", "HXA", "HAMZAVIP", "ILYAS_KH_YT_TOP"]
    
    # Keys load karna
    with open("all_keys.txt", "r") as f:
        keys = [l.strip() for l in f.readlines() if l.strip()]

    # Index (Ginti) read karna
    with open("index.txt", "r") as f:
        index = int(f.read().strip())

    # Agli key uthana
    current_key = keys[index % len(keys)]
    chosen_prefix = random.choice(prefixes)
    
    # Final Masked Key (Jo user ko dikhegi)
    # Example: HXA_SN05_KEY123
    session_no = f"SN{index+1:02d}"
    final_output = f"{chosen_prefix}_{session_no}_{current_key}"

    # key.txt (Public file) mein likhna
    with open("key.txt", "w") as f:
        f.write(final_output)

    # Agli baar ke liye index+1 karna
    with open("index.txt", "w") as f:
        f.write(str((index + 1) % len(keys)))

if __name__ == "__main__":
    rotate()
  
