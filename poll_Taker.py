import itertools
import random
import time

DESTINATIONS = ["Sedona", "Joshua Tree", "Zion", "San Francisco"]
SPINNER_FRAMES = ["|", "/", "-", "\\"]


def spin_for_choice(options):
    """Animate a spinner and land on the randomly selected option."""
    selected = random.choice(options)
    frame_cycle = itertools.cycle(SPINNER_FRAMES)
    index_cycle = itertools.cycle(range(len(options)))
    steps = random.randint(25, 40)
    current_index = next(index_cycle)

    print("Spinning for your next destination...")
    time.sleep(0.4)  # brief pause before the spinner starts

    for step in range(steps):
        frame = next(frame_cycle)
        current_option = options[current_index]
        print(f"\r{frame} Spinning... {current_option:<20}", end="", flush=True)
        time.sleep(0.08 + step * 0.004)
        current_index = next(index_cycle)

    while options[current_index] != selected:
        frame = next(frame_cycle)
        current_option = options[current_index]
        print(f"\r{frame} Spinning... {current_option:<20}", end="", flush=True)
        time.sleep(0.12)
        current_index = next(index_cycle)

    for _ in range(3):
        frame = next(frame_cycle)
        print(f"\r{frame} Spinning... {options[current_index]:<20}", end="", flush=True)
        time.sleep(0.15)

    print(f"\r[+] Selected: {selected:<20}")


if __name__ == "__main__":
    spin_for_choice(DESTINATIONS)
