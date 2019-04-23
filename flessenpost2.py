from code.helperfunctions.possiblemoves import checkmove, possiblemovesA
from code.helperfunctions.assign import assign
import random


def sortparcels(parcellist):
    sorted_parcels = sorted(parcellist, key=lambda cargo: cargo.mass, reverse=False)
    return sorted_parcels

def sortspacecrafts(shiplist):
    sorted_ships = sorted(shiplist, key=lambda spacecraft: spacecraft.payload, reverse=False)
    return sorted_ships

def dofirstmove(shiplist, extralist):
    possiblelist =[1]
    while len(possiblelist) != 0:
        possiblelist = possiblemovesA(shiplist, extralist)
        print(f"possiblelist = {possiblelist}")
        if len(possiblelist) == 0:
            break
        chosenmove = possiblelist[0]
        assign(chosenmove[0], chosenmove[1])
        extralist.remove(chosenmove[1])
    #print(f"space0 assigned/weight/vol: {shiplist[0].name}{len(shiplist[0].assigned)}/{shiplist[0].payload}/{shiplist[0].volume}")
    #print(f"space1 assigned/weight/vol: {shiplist[1].name}{len(shiplist[1].assigned)}/{shiplist[1].payload}/{shiplist[1].volume}")
    #print(f"space2 assigned/weight/vol: {shiplist[2].name}{len(shiplist[2].assigned)}/{shiplist[2].payload}/{shiplist[2].volume}")
    #print(f"space3 assigned/weight/vol: {shiplist[3].name}{len(shiplist[3].assigned)}/{shiplist[3].payload}/{shiplist[3].volume}")
    print(f"remainders na herverdeling: {len(extralist)}")

def flessenpost2(shiplist, parcellist):
    sorted_parcels = sortparcels(parcellist)
    sorted_ships = sortspacecrafts(shiplist)
    remainders = []

    for ship in range(len(sorted_ships)):
        for parcel in range(len(sorted_parcels)):
            print(f"parcel {parcel}")
            print(f"lengthparcels {len(sorted_parcels)}")
            if sorted_parcels[parcel].mass > 370:
                print("te groot")
            elif checkmove(sorted_parcels[parcel], sorted_ships[ship]):
                assign(sorted_ships[ship], sorted_parcels[parcel])
                sorted_parcels.remove(sorted_parcels[parcel])
        #else:
            #remainders.append(sorted_parcels[parcel])

    print(f"remainders initieel: {len(sorted_parcels)}")
    print("---------------------------------------")
    #print(f"space0 assigned/weight/vol: {sorted_ships[0].name}{len(sorted_ships[0].assigned)}/{sorted_ships[0].payload}/{sorted_ships[0].volume}")
    #print(f"space1 assigned/weight/vol: {sorted_ships[1].name}{len(sorted_ships[1].assigned)}/{sorted_ships[1].payload}/{sorted_ships[1].volume}")
    #print(f"space2 assigned/weight/vol: {sorted_ships[2].name}{len(sorted_ships[2].assigned)}/{sorted_ships[2].payload}/{sorted_ships[2].volume}")
    #print(f"space3 assigned/weight/vol: {sorted_ships[3].name}{len(sorted_ships[3].assigned)}/{sorted_ships[3].payload}/{sorted_ships[3].volume}")
    #print(possiblemovesA(shiplist, remainders))
    dofirstmove(shiplist, sorted_parcels)
