#print("Cool")
cool_number = 1
not_cool_number = 6
#print(cool_number + not_cool_number)
kesh = ["Enyo", "Kai", "Lenne"]
#print(kesh)
veggies = [["lettuce", 4], ["tomatoes", 3.50]]
#print(veggies)
for element in kesh:
    print(element) 
for i in range(1,len(kesh)):
    print(i)
    print(kesh[i])
check = 5
if check >= 5 and check < 6:
    print("Funny Number")
else:
    print("cringe")
funny_word = "Ok"
if funny_word != "Ok":
    print("Not Ok")
else:
    print("All good")    

def funny_function(sentence):
    print(sentence)

funny_function("Ciao")

def sum_numbers(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

sum_numbers(cool_number,not_cool_number)
cool_number = 4
not_cool_number = 3.4
sum_numbers(cool_number,not_cool_number)
sum_numbers(kesh,kesh)
g = 0
while g<5:
    print("It is under five")
    g += 1
hello = "Hello World"
for element in hello:
    print(element)

def encrypt(sentence,key):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    result = f""
    for element in sentence:
        elem_index = alphabet.index(element)
        new_index = elem_index + key
        new_letter = alphabet[new_index]
        result = f"{result}{new_letter}"
    return result    
test = "CIAO"
result = encrypt(test,1)
print(result)