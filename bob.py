import math
from keyGenerator import keyGenerator

class Bob:

    def __Keys(self):
        generator = keyGenerator()
        global e,N,_composite
        e,N,_composite = generator.getKeys()

    
    def publishKeys(self):
        self.__Keys()
        return e,N
    
    def __decryptionExponent(self):
        d = pow(e,-1,_composite)
        return d
        

    def decrypt(self, encrypted_int):
        d = self.__decryptionExponent()
        
        decrypted = pow(encrypted_int, d, N)

        length = math.ceil(math.log(decrypted)/math.log(256))
        message = decrypted.to_bytes(length, "little").decode()

        return message

        


