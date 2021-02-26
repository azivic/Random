import datetime

class BikeRental:
    
    def __init__(self,stock=0):
        #klasa konstruktora koja pokreće prodavnicu iznajmljivanja bicikala 
        self.stock = stock

    def displaystock(self):
         #Prikazuje bicikle koji su trenutno dostupni za iznajmljivanje 
       

        print("Trenutno je na raspolaganju {} bicikala za iznajmljivanje".format(self.stock))
        return self.stock

    def rentBikeOnHourlyBasis(self, n):
      
        if n <= 0:
            print("Broj bicikala za iznajmljivanje mora biti najmanje 1.")
            return None
        
        elif n > self.stock:
            print("O ne! Trenutno na raspolaganju nemamo {} bicikala za iznajmljivanje.".format(self.stock))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("Iznajmili ste {} komada na jedan sat, pocevsi od danas u {} casova.".format(n,now.hour))
            print("Bice Vam naplaceno 200 dinara po biciklu. \n Ukoliko prekoracite vreme, cena ce biti svakog sata uvecana za 500 dinara, za svaki bicikl")
            print("Nadamo se da cete uzivati!")

            self.stock -= n
            return now      
     
    def rentBikeOnDailyBasis(self, n):
       
        if n <= 0:
            print("Broj bicikala za iznajmljivanje mora biti najmanje 1.")
            return None

        elif n > self.stock:
            print("O ne! Trenutno na raspolaganju nemamo {} bicikala za iznajmljivanje.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("Iznajmili ste {} komada na jedan dan, pocevsi od danas u {} casova.".format(n,now.hour))
            print("Bice Vam naplaceno 800 dinara po biciklu. \n Ukoliko prekoracite vreme, cena ce biti svakog sata uvecana za 500 dinara, za svaki bicikl")
            print("Nadamo se da cete uzivati!")


            self.stock -= n
            return now
        
    def rentBikeOnWeeklyBasis(self, n):
        if n <= 0:
            print("Broj bicikala za iznajmljivanje mora biti najmanje 1.")
            return None

        elif n > self.stock:
            print("O ne! Trenutno na raspolaganju nemamo {} bicikala za iznajmljivanje.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("Iznajmili ste {} komada na 7 dana, pocevsi od danas u {} casova.".format(n,now.hour))
            print("Prilikom vracanja bice Vam naplaceno 2000 dinara po biciklu. \n Ukoliko prekoracite vreme, cena ce biti svakog sata uvecana za 500 dinara, za svaki bicikl")
            print("Nadamo se da cete uzivati!")


            self.stock -= n
            return now

    
    def returnBike(self, request):
        """
        1. Prihvatiti iznajmljen bicikl od korisnika
        2. Dopuniti inventar
        3. Isporuciti racun
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # sat
            if rentalBasis == 1:
                print("Koristili ste ", rentalPeriod)
                bill = round(rentalPeriod.seconds / 3600) * 200 * numOfBikes
                
            # dan
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 800 * numOfBikes
                
            # nedelja
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 2000 * numOfBikes
            
               
            if (3 <= numOfBikes <= 5):
                print("Ostvarili ste 30% popusta na iznajmljivanje!")
                bill = bill * 0.7

            print("Hvala sto ste koristili nasu prodavnicu!")
            print("Vas racun je: {} dinara".format(bill))
            return bill
        else:
            print("Da li ste sigurni da ste iznajmili bicikle iz nase prodavnice?")
            return None



class Customer:

    def __init__(self): 
        #Konstruktorski metod koji instancira različite korisničke objekte.
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
        #Uzima zahtev od kupca za trazeni broj bicikala.
        
                      
        bikes = input("Koliko bicikala zelite da iznajmite?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Pogresan unos!")
            return -1

        if bikes < 1:
            print("Pogresan unos!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        #Omogucava korisnicima da vrate svoj bicikl.
        
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
