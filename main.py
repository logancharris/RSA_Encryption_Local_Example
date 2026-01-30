from alice import Alice
from bob import Bob


def main():
    B = Bob()
    e,N = B.publishKeys()

    print("Bob publishes his public encryption keys")
    print("e = ", e)
    print("N = ", N)

    A = Alice(e,N)
    m = "Hello Bob!"
    encrypted_message = A.encrypt(m)

    print("Using these public keys Alice sends the encrypted message: ", encrypted_message)
    print("IMPORTANT: The integer representation of Alice's message before encryption must be shorter than N. Otherwise the message won't properly encrypt and decrypt.")

    message = B.decrypt(encrypted_message)

    print("Using his private keys Bob decrypts the message to say:", message)

if __name__ == "__main__":
    main()
