import csv
from itertools import combinations

billsList = []
transferList = []

class Bill:
    def __init__(self, amount, description, date):
        self._amount = amount
        self._descr = description
        self._date = date
    def __str__(self):
        return self._descr + ": " + str(self._amount) + " vom " + self._date
class Transfer:
    def __init__(self, amount, date):
        self._amount = amount
        self._date = date
    def __str__(self):
        return str(self._amount) + " vom " + self._date

def calculateBill(bills, transfers):
    if (bills.__len__() != 0 and transfers.__len__() != 0):
        for i in transfers:
            bestFitBills = ()
            bestFitBillsSum = 0
            skip = False
            for j in range(1, bills.__len__()+1):
                comb = combinations(bills, j)
                for k in list(comb):
                    oldSumOfBills = 0
                    sumOfBills = 0
                    if (not skip):
                        for l in k:
                            sumOfBills += float(l._amount)
                            if (sumOfBills == i._amount):
                                bestFitBills = k
                                bestFitBillsSum = sumOfBills
                                skip = True # Skip, cause Bills found
                            elif (sumOfBills < i._amount and sumOfBills > bestFitBillsSum):
                                bestFitBillsSum = sumOfBills
                                bestFitBills = k
                            elif (sumOfBills > i._amount):
                                sumOfBills = oldSumOfBills
                            oldSumOfBills = sumOfBills
            print("")
            print("Überweisung: " + str(i._amount) + " vom " + i._date)
            print("gefundener, passender Betrag: " + str(bestFitBillsSum))
            print("passende Rechnungen: ")
            for l in bestFitBills:
                print(l.__str__())
            print("-------------------------------------------------------------------------")

    else:
        print("Error: Leere Rechnungs- oder Überweisungsliste!")


def readBills(filename):
    with open(filename, "rt", encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            billsList.append(Bill(float(row[0]),row[1],row[2]))

def readTransfers(filename):
    with open(filename, "rt", encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            transferList.append(Transfer(float(row[0]),row[1]))

if __name__ == '__main__':
    readBills('bills.csv')
    readTransfers('transfers.csv')
    print("")
    print("Rechnungen: ")
    for i in billsList:
        print(i.__str__())
    print("")
    print("Überweisungen: ")
    for i in transferList:
        print(i.__str__())
    print("")
    print("Kalkulation: ----------------------------------------")
    calculateBill(billsList, transferList)