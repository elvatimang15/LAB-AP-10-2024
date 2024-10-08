def palindrome (kata) :

    kata = kata.lower()
    
    if kata == kata[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

palindrome ("papa")
