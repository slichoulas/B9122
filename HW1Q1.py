#Sophia Lichoulas Problem Set One.

#Question 1
# Description: Calculates Equated Monthly Installment of a loan
# Input Parameters: takes as parameters integers principal amount and future value from user and default parameters rate and number of periods
# Returns EMI value, as a float
def compute_emi(rate=.04, N=20, PV=0, FV=0):
    #Takes input for PV and FV; use try/except to vaidate type.

    #Get Integer PV
    while(1):
        try:
            PV = int(input("Please enter an integer for principal amount: "))
        except:
            print("Not an integer! Try again")
        else:
            break

    #Get Integer FV:
    while(1):
        try:
            FV = int(input("Please enter an integer for future value amount: "))
        except:
            print("Not an integer! Try again")
        else:
            break

    #calculate EMI
    PV = float(PV)
    FV = float(FV)

    #broke down EMI calculation for clarity
    x1 = PV + (FV / ( 1 + rate) ** N)
    x2 = (rate * (1 + rate) ** N)
    x3 = (1 + rate) ** N - 1

    emi = x1*x2/x3
    print('final check: : emi is', emi)  #debugging code, delete later
    return emi

compute_emi()

