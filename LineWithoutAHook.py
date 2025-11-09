import time
import sys

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- Reff "Line Without a Hook" ---
reff = [
    ("\nOh, baby, I am a wreck when I'm without you\n", 0.1),
    ("I need you here to stay...\n", 0.13),
    ("I broke all my bones that day I found you\n", 0.1),
    ("Crying at the lake...\n", 0.1),
    ("\nWas it something I said to make you feel like you're a burden?\n", 0.1),
    ("Oh, and if I could take it all back, I swear that I\n", 0.1),
    ("Would pull you from the tide...\n", 0.1)
]

for line, delay in reff:
    type_text(line, delay)
    time.sleep(0.3)
