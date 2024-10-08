input_string = input("Input your string: ")  

def generate_substrings(s):  
    substrings = []  
    length = len(s)  

    
    for i in range(length):  
        for j in range(i + 1, length + 1):  
            substrings.append(s[i:j])  
    
    return substrings  


substrings = generate_substrings(input_string)  

print("===============================")  
for substring in substrings:  
    print(substring)  
print("===============================")  