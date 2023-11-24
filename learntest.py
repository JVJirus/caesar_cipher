def encrypt(sentence,key):
    result = f""
    for element in sentence:
        conversion = ord(element)
        
        if conversion >= 65 and conversion <= 90:
           new_index = (conversion - 65 + key) % 26 + 65
        elif conversion >= 97 and conversion <= 122:
           new_index = (conversion - 97 + key) % 26 + 97
        else:
            new_index = conversion
            
            
        new_letter = chr(new_index)
        result = f"{result}{new_letter}"    
    
    return result    

Text = input("Your string here ") #We want to read the input
#key = input("Select your Key value ") #They can choose the key || They cannot cuz we cant add a string and an int 
 

     
   
   
#if test.isnumeric() == True: # I dont want only numbers /  anyway useless cuz now we also accept numbers with the IF
    #test = input("No numbers please, retry. Your String here ")
#test = test.upper() #Just to guarantee the function finds the correct letter, downside is all results will all be uppercase / obsolete cuz we fixed it by adding lower uppcase letter in list
result = encrypt(Text,1)
print(result)

