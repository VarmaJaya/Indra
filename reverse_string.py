string = input("please enter your string: ")

# # varma = indra[-1]+indra[-2]+indra[-3]+indra[-4]+indra[-5]
'''
# first method
v = -len(string)  # assuming len(indra) is 5
new_string = ""
for i in range(-1, v-1, -1):
    new_string+=string[i]
print(f"the reverse of string: {new_string}")

if string == new_string:
    print("Ploynodrom")
else:
    print("The given string is not a polyndrome")
'''


new_string = string[::-1]
print(f"the reverse of string: {new_string}")
if string == new_string:
    print("Ploynodrom")
else:
    print("The given string is not a polyndrome")

    
 