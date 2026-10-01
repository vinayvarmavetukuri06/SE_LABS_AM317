def evaluate(target, guess):
    result = ["gray"] * len(guess)

    # First pass: resolve exact matches.
    remaining = list(target)

    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[i] = None

    # Second pass: resolve misplaced letters.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if ch in remaining:
            result[i] = "yellow"
            remaining[remaining.index(ch)] = None

    return result