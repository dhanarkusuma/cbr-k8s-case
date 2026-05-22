def numeric_similarity(a, b, max_value=100):
    return 1 - (abs(a - b) / max_value)
