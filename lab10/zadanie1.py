def wypisz_slownik(slownik):
    for klucz in slownik:
        print(f"{klucz} {slownik[klucz]}")


oceny = {
    1: "niedostateczny",
    1.5: "niedostateczny plus",
    2: "dopuszczający",
    2.5: "dopuszczający plus",
    3: "dostateczny",
    3.5: "dostateczny plus",
    4: "dobry",
    4.5: "dobry plus",
    5: "bardzo dobry",
    5.5: "bardzo dobry plus",
    6: "celujący"
}

print("Oceny w szkole średniej:")
wypisz_slownik(oceny)

# Teraz zmienie slownik oceny zeby zawieral tylko te oceny co są na UG

oceny.pop(1)
oceny.pop(1.5)
oceny.pop(5.5)
oceny.pop(6)
print()

print("Oceny na UG:")
wypisz_slownik(oceny)
