def remove_prefix(s: str, prefix="\n\n"):
    s = s.lstrip()
    return s.removeprefix(prefix)
