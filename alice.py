class Alice:
    def __init__(self, E, n):
        global e, N
        e = E
        N = n

    def encrypt(self, m) -> int:
        message = m
        
        m_int = int.from_bytes(message.encode(), "little")

        c = (m_int ** e)% N
        
        return c
    