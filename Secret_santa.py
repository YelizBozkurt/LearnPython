import random

nouns = ["Suna","Elif","Ayşe","Zeynep","Yağmur","Sude"]

def gifts_raffle():
    recipients = nouns.copy()
    givers = nouns.copy()


    while len(recipients) >0 :

        buyer_index = random.randint(0,len(recipients)-1)
        transmitter_index = random.randint(0,len(givers)-1)

        while recipients[buyer_index]== givers[transmitter_index]:
              buyer_index = random.randint(0, len(recipients) - 1)
              transmitter_index = random.randint(0, len(givers) - 1)

        print(recipients[buyer_index],"Şu kişiye hediye alacak: ",givers[transmitter_index])

        del recipients[buyer_index]
        del givers[transmitter_index]




gifts_raffle()
