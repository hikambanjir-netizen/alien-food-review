"""One Star, Five Stars for the Food — an alien tourist's one-star
review of Earth that still slips in a real compliment about the food.

The grievance is the bafflement: a planet that charges rent for
sleeping indoors. The turn is the food: twelve dumplings in, and the
reviewer is briefly considering citizenship.
"""

LINE = "I gave Earth one star because the locals charge rent for sleeping indoors, yet the dumplings were so good I ate twelve and briefly considered citizenship."

import os

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass

print(LINE)
