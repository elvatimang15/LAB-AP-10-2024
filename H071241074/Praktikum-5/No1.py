def palindrome(kalimat):
    kalimat = kalimat.lower()

    if kalimat == kalimat[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


palindrome("Besok")

