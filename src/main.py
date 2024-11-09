import shoresh

mode = input("what do you want to do? \n a) practice old words \n b) add info to old words \n c) create new word \n")
if mode == "c":
    l1 = input("first letter of shoresh: ")
    l2 = input("second letter of shoresh:  ")
    l3 = input("third letter of shoresh: ")

    meaning = input("meaning: ")
    impshrsh = shoresh.Shoresh([l1, l2, l3], meaning)
    past = impshrsh.autoConjugatePaal("Past")
    pres = impshrsh.autoConjugatePaal("Present")
    futr = impshrsh.autoConjugatePaal("Future")
    inf = impshrsh.autoConjugatePaal("Infinitive")
    imp = impshrsh.autoConjugatePaal("Imperative")

    impshrsh.addShoresh()
    impshrsh.addBinyan("Pa'al")
    impshrsh.binyanInfo("Pa'al", inf, past, pres, futr, imp, meaning)



