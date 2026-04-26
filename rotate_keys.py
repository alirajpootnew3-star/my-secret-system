import os
import random

def rotate():
    prefixes = ["ILYAS_KH_YT", "HXA", "HAMZAVIP", "ILYAS_VIP"]
    
    # All Keys load karna
    if not os.path.exists("all_keys.txt"): return
    with open("all_keys.txt", "r") as f:
        # split() use kiya hai taaki space ya new line ka masla na ho
        keys = f.read().split()

    if not keys: return

    # Index manage karna
    index = 0
    if os.path.exists("index.txt"):
        with open("index.txt", "r") as f:
            index = int(f.read().strip())

    # Key pick karna
    current_key = keys[index % len(keys)]
    chosen_prefix = random.choice(prefixes)
    session_no = f"SN{index+1:02d}"
    
    # FINAL KEY (Bina kisi extra space ke)
    final_output = f"{chosen_prefix}_{session_no}_{current_key}".strip()

    with open("key.txt", "w") as f:
        f.write(final_output)

    with open("index.txt", "w") as f:
        f.write(str((index + 1) % len(keys)))

if __name__ == "__main__":
    rotate()
