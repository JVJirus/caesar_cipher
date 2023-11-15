def encrypt(sentence,key):
    #alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"] old
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    #alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z","1","2","3","4","5","6","7","8","9","0"] Test to see if it sees numbers now, ok no like this it also applies the key to numbers
    result = f""
    for element in sentence :
        if element.isalpha() and element in alphabet :
           elem_index = alphabet.index(element)
           new_index = (elem_index + key) % len(alphabet)
           new_letter = alphabet[new_index]
           result = f"{result}{new_letter}"
        else:
            result = f"{result}{element}"    
    
    return result    

Text = input("Your string here ") #We want to read the input
#key = input("Select your Key value ") #They can choose the key || They cannot cuz we cant add a string and an int 
 

     
   
   
#if test.isnumeric() == True: # I dont want only numbers /  anyway useless cuz now we also accept numbers with the IF
    #test = input("No numbers please, retry. Your String here ")
#test = test.upper() #Just to guarantee the function finds the correct letter, downside is all results will all be uppercase / obsolete cuz we fixed it by adding lower uppcase letter in list
result = encrypt(Text,1)
print(result)