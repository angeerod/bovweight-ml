"""
Bovine weight estimation using the Schoorl formula variant adapted for
Bos taurus cattle common in Costa Rica:
    Weight (kg) = (Girth_cm ^ 2 * Length_cm) / 10800
"""


def estimate_weight(height_cm: float, length_cm: float, girth_cm: float) -> float:
    if any(v <= 0 for v in [height_cm, length_cm, girth_cm]):
        raise ValueError("All measurements must be positive numbers.")
    # Height is captured for future model improvement; formula uses girth & length.
    return (girth_cm ** 2 * length_cm) / 10800
