# Caesar cipher
def cipherfn(text, code_val):
    cipher = ''
    for char in text:
        code=ord(char)
        if char.isalpha():
            print(chr(code))
            code+=code_val-1
            if code > ord('z'):
                code = (code - ord('z') )+ord('a') 
            elif code > ord('Z'):
                code = (code - ord('Z')  )+ord('A') 
            #code+=code_val
        cipher += chr(code)
    return cipher

#text = input("Enter your message: ")

code_val = 0
try:
    while code_val <= 25:
        code_val = int(input("Number to be added: "))
        print(cipherfn(text,code_val))
except:
    print("Enter a value between 1 and 25")
