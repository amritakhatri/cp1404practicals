import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))

# Function to generate a single quick pick
def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))

# Generate and display the quick picks
for _ in range(NUM_QUICK_PICKS):
    quick_pick = generate_quick_pick()
    print(" ".join(map(str, quick_pick)))
