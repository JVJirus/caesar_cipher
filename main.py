import argparse
from Src.caesar_cipher import *

#this is the entry point of the program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description= "encrypt and decrypts through a cipher key"
    )
    parser.add_argument(
        '--sentence',
        '-s',
        action="store",
        default=None,
        dest= "request"
        )
    parser.add_argument(
        '--key',
        '-k',
        type=int,
        action="store",
        default= 1,
        dest="key"
        )
    parser.add_argument(
        '--path',
        '-p',
        type=str,
        default=None,
        action="store",
        dest = "complex_request"
    )
    args = parser.parse_args()
    print(args)    
    Cyper = Caesar(args.request,args.key,args.complex_request)
    if args.request is not None and args.complex_request is None:
        result_encryption = Cyper.encrypt_sentence()
        print(result_encryption)
        result_decryption = Cyper.decrypt_sentence(request=result_encryption)
        print(result_decryption)
    elif args.request is None and args.complex_request is not None:
        Cyper.encrypt_file()
    else:
        print("No argument input, please retry")       
