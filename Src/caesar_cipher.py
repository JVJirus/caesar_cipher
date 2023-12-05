from Src.utils import encrypt,decrypt
class Caesar:
    def __init__(self,sentence,key,inputpath):
        self.sentence = sentence
        self.key = key
        self.inputpath = inputpath
    def encrypt_sentence(self):
        result = encrypt(self.sentence,self.key)
        return result
    def decrypt_sentence(self,request):
        result = decrypt(request,self.key)
        return result
    def encrypt_file(self):
        with open(self.inputpath, 'r') as file:
            for line in file:#.readline()
                
                line_encryption = encrypt(line,self.key)
                #print(line_encryption)
                with open("./Assets/output.txt",'a') as newfile:
                    newfile.write(line_encryption)
            
                