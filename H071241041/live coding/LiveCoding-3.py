def stringPermutation(word):
    try:
        if not isinstance(word, str):
            raise TypeError("Input harus berupa string")
        
        # | sebagai pemisah
        return ' | '.join([word[i:] + word[:i] for i in range(len(word))]) + ' |'
    
    except TypeError as te:
        return str(te)

print(stringPermutation("Oval"))
