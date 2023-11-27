def parrot(string=None):
    if  string is not None and string  == f"{string}":
        print(f"{string}")
        return string
    else:
        print("Squawk!")
        return "Squawk!"


parrot("Mankulo")

parrot()
