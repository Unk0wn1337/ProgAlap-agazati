def elsoFeladat():
    print("\nI/A,B")
    etelNev = input("\n\tÉtel neve:")
    ertekelesRendelo = input("\tÉtel rendelőjének neve: ")
    ertekeles = int(input("\tÉrtékelés (1-5): "))
    if ertekeles <= 0:
        print("\tAz értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("\t5 pont feletti értékelés nem elfogadható!")
    else:
        print("\tKöszönjük az értékelést")