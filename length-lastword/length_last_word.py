
def length_of_last_word(s: str) -> int:
        s=s.strip()
        s=s.split(' ')
        return len(s[-1])