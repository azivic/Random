from bikeRental import BikeRental, Customer

def main():
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Iznajmljivanje bicikala =======
        1. Broj dostupnih bicikala
        2. Iznajmi bicikl na 1 sat 
        3. Iznajmi bicikl na 1 dan
        4. Iznajmi bicikl na 7 dana
        5. Vrati bicikl
        6. Odustani
        """)
        
        choice = input("\n Izaberite opciju: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Niste uneli broj!\n")
            continue
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Neispravan unos. Unesite broj od 1 do 6. \n")        
    print("\n Hvala sto koristite nas sistem iznajmljivanja!")


if __name__=="__main__":
    main()