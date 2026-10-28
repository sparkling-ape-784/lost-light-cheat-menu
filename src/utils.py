# Build: ad6c46522d1b7c3e9fc94aa15ee0c209

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
