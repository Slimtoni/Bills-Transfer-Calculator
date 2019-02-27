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
        return str(self._amount) + " | " + self._descr + " | " + self._date
class Transfer:
    def __init__(self, amount, date):
        self._amount = amount
        self._date = date
    def __str__(self):
        return str(self._amount) + " | " + self._date

# DEPRECATED
# def calculateBill(billsList, transferList):
#     if (billsList.__len__() != 0 and transferList.__len__() != 0):
#         for i in transferList:
#             oldSumOfBills = 0
#             sumOfBills = 0
#             bestFitBills = []
#             bestFitBillsSum = 0
#             for j in billsList:
#                 sumOfBills += j._amount
#                 if (sumOfBills == i._amount):
#                     bestFitBills.append(j)
#                     bestFitBillsSum = sumOfBills
#                 elif (sumOfBills > i._amount):
#                     bestFitBill = oldSumOfBills
#                     break
#                 elif (sumOfBills < i._amount and sumOfBills > bestFitBillsSum):
#                     bestFitBills.append(j)
#                     continue
#                 oldSumOfBills = sumOfBills
#             for bills in bestFitBills:
#                 print(bills.__str__())
#     else:
#         print("Error: Leere Rechnungs- oder Überweisungsliste!")

def calculateBill2(bills, transfers):
    if (bills.__len__() != 0 and transfers.__len__() != 0):
        for i in transfers:
            oldSumOfBills = 0
            bestFitBills = ()
            bestFitBillsSum = 0
            billfound = False
            for j in range(1, bills.__len__()+1):
                if (not billfound):
                    #print("-------------------------------------------------------------")
                    comb = combinations(bills, j)
                    for k in list(comb):
                        sumOfBills = 0
                        #print("Tupel: ---------------------------------------------")
                        for l in k:
                            sumOfBills += float(l._amount)
                            if (sumOfBills == i._amount):
                                bestFitBills = k
                                bestFitBillsSum = sumOfBills
                                billfound = True
                            if (sumOfBills < i._amount and sumOfBills > bestFitBillsSum):
                                bestFitBillsSum = sumOfBills
                                bestFitBills = k
                    billfound = True
            print("SumOfBills: " + str(sumOfBills))
            for l in bestFitBills:
                print(l.__str__())
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
    readBills('bills_test.csv')
    readTransfers('transfers_test.csv')
    print("Rechnungen: ")
    for i in billsList:
        print(i.__str__())
    print("Überweisungen: ")
    for i in transferList:
        print(i.__str__())

    print("Kalkulation: ")
    calculateBill2(billsList, transferList)