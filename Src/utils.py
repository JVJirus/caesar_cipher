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

def decrypt(sentence,key):
    result = f""
    for element in sentence:
        conversion = ord(element)
        
        if conversion >= 65 and conversion <= 90:
           new_index = (conversion - 65 - key + 26) % 26 + 65
        elif conversion >= 97 and conversion <= 122:
           new_index = (conversion - 97 - key + 26) % 26 + 97
        else:
            new_index = conversion
            
            
        new_letter = chr(new_index)
        result = f"{result}{new_letter}"    
    
    return result    