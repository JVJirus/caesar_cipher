import argparse

#this is the entry point of the program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description= "encrypt and decrypts through a cipher key"
    )
    parser.add_argument(
        '--sentence',
        '-s',
        action="store",
        dest= "request"
        )
    parser.add_argument(
        '--key',
        '-k',
        type=int,
        action="store",
        dest="key"
        )
    args = parser.parse_args()
    print(args)    