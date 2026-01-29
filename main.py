from alice import Alice
from bob import Bob


def main():
    B = Bob()
    e,N = B.publishKeys()

    print("Bob publishes his public encryption keys")
    print("e = ", e)
    print("N = ", N)

    A = Alice(e,N)
    m = "a"
    encrypted_message = A.encrypt(m)

    print("Using these public keys Alice sends the encrypted message: ", encrypted_message)

    message = B.decrypt(encrypted_message)

    print("Using his private keys Bob decrypts the message to say: ", message)


if __name__ == "__main__":
    main()
