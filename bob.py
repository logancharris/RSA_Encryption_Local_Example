import math
from keyGenerator import keyGenerator

class Bob:
    
    def publishKeys(self):
        generator = keyGenerator()
        global e,N,_composite
        e,N,_composite = generator.getKeys()
        return e,N
    
    def __decryptionExponent(self):
        
        for i in range(2,_composite):
            if (i*e %_composite == 1):
                d = i
                break
        return d
        

    def decrypt(self, encrypted_int):
        d = self.__decryptionExponent()
        
        decrypted = (encrypted_int ** d) % N

        length = math.ceil(math.log(decrypted)/math.log(256))
        message = decrypted.to_bytes(length, "little").decode()

        return message

        


