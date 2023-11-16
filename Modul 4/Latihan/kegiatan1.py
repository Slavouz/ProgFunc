def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

def main():
    firstnum = perkalian(3)
    hasil = firstnum(5) #HoF
    print(hasil)
    print(perkalian(2)(4)) #currying

if __name__ == "__main__":
    main()