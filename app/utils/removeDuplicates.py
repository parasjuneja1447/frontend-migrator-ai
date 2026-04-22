def     remove_duplicates(components):
    seen = set()
    unique = []

    for comp in components:
        key = str(comp)
        if key not in seen:
            seen.add(key)
            unique.append(comp)

    return unique