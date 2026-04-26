import os
import random

def rotate():
    prefixes = ["ILYAS_KH_YT", "HXA", "HAMZAVIP", "ILYAS_KH_YT_TOP"]
    
    if not os.path.exists("all_keys.txt"): return

    with open("all_keys.txt", "r") as f:
        # Sirf pehli key pick karne ke liye filter
        keys = [line.strip() for line in f.read().split() if line.strip()]

    if not keys: return

    index = 0
    if os.path.exists("index.txt"):
        with open("index.txt", "r") as f:
            index = int(f.read().strip())

    current_key = keys[index % len(keys)]
    chosen_prefix = random.choice(prefixes)
    session_no = f"SN{index+1:02d}"
    
    # Final Output: Sirf ek prefix aur ek key
    final_output = f"{chosen_prefix}_{session_no}_{current_key}"

    with open("key.txt", "w") as f:
        f.write(final_output)

    with open("index.txt", "w") as f:
        f.write(str((index + 1) % len(keys)))

if __name__ == "__main__":
    rotate()
