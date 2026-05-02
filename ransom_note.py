def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # TODO: Implement this function
    counts = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in ransomNote:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1

    return True

