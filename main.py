from Helper import *
from Loan import *
from LoanPortfolio import *
from LoanImpacts import *

loans = LoanPortfolio()


def compute_schedule(principal, rate, term, extra_payment):

    loan = None
    try:
        loan = Loan(principal=principal, rate=rate, term=term, extra_payment=extra_payment)
        loan.check_loan_parameters()
        loan.compute_schedule()
    except ValueError as ex:
        print(ex)
    loans.add_loan(loan)
    #return Helper.print(loan), Helper.plot(loan)

    #print(round(loan.total_principal_paid, 2), round(loan.total_interest_paid, 2), round(loan.time_to_loan_termination, 0))

    if loans.get_loan_count() == 3:
        loans.aggregate()
        #Helper.plot(loans)
        Helper.print(loans)

        #print(round(loan.total_principal_paid, 2), round(loan.total_interest_paid, 2),round(loan.time_to_loan_termination, 0))



#compute_schedule(27000.0, 4.0, 24, 0.0)
#compute_schedule(27000.0, 4.0, 24, 25.0)
#compute_schedule(10000.0, 3.0, 24, 7.0)

#principal = 10000
#rate = 4
#term = 24
#extra_payment = 0
#contributions = [100, 100]
#loan_impacts = LoanImpacts(principal=principal, rate=rate, term=term,
                           #extra_payment=extra_payment, contributions=contributions)
#loan_impacts.compute_impacts()