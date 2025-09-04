from script.factory import GameFactory

import time
import sys

def slow_print(text, delay=0.005):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_sequence(boot_sequence):
    for line in boot_sequence:
        slow_print(line, delay=0.05)
        time.sleep(0.2)

if __name__ == "__main__":
    print(r"""
 /$$$$$$$            /$$           /$$       /$$          
| $$__  $$          |__/          |__/      | $$          
| $$  \ $$  /$$$$$$  /$$  /$$$$$$$ /$$  /$$$$$$$  /$$$$$$ 
| $$  | $$ /$$__  $$| $$ /$$_____/| $$ /$$__  $$ /$$__  $$
| $$  | $$| $$$$$$$$| $$| $$      | $$| $$  | $$| $$$$$$$$
| $$  | $$| $$_____/| $$| $$      | $$| $$  | $$| $$_____/
| $$$$$$$/|  $$$$$$$| $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$
|_______/  \_______/|__/ \_______/|__/ \_______/ \_______/  
""")
    slow_print(">>> Human Benchmark AutoBot | Mode: H4x0r\n", delay=0.001)

    slow_print("[*] Initializing bot...")
    slow_print("[*] Loading neural subroutines...")
    slow_print("[*] Calibrating mouse control unit...")
    slow_print("[✓] Ready to dominate Human Benchmark.\n")

    slow_print("Select your mission:\n")
    slow_print(" [1] Reaction Time Override")
    slow_print(" [2] Sequence Memory Hack")
    slow_print(" [3] Aim Trainer Aimbot (BETA)")
    slow_print(" [4] Exit the matrix\n")

    value = int(input())
    seq = GameFactory.get_game(value)

    boot_sequence = []

    if seq.start():
        boot_sequence = [
            "[BOOT] System check... OK",
            "[BOOT] Injecting Python core",
            "[BOOT] Accessing HumanBenchmark API... [APPROVED]",
            "[HACK] Bypassing security... [OK]",
            "[AI] Neural bot interface online.",
            "[READY] Loading your weapon."
        ]
        print_sequence(boot_sequence)
        seq.set_settings()
        seq.play()
    else :
        boot_sequence = [
            "[BOOT] System check... ERROR",
            "[BOOT] Accessing HumanBenchmark API... [DENIED]",
            "[HACK] Bypassing security... [ERROR]",
            "[AI] Neural bot interface offline.",
        ]
        print_sequence(boot_sequence)

    