from Helper import *
from Loan import *
from LoanPortfolio import *
from LoanImpacts import *
import pandas as pd

n_clicks = True
principal, interest, term, extra = 27000.0, 4.0, 24, 0.0
principal1, interest1, term1, extra1 = 27000.0, 4.0, 24, 25.0
principal2, interest2, term2, extra2 = 10000.0, 3.0, 24, 7.0

if n_clicks is not None:

    loan0 = Loan(principal=float(principal), rate=float(interest), term=float(term), extra_payment=float(extra))
    loan1 = Loan(principal=float(principal1), rate=float(interest1), term=float(term1), extra_payment=float(extra1))
    loan2 = Loan(principal=float(principal2), rate=float(interest2), term=float(term2), extra_payment=float(extra2))
    loans = [loan0,loan1,loan2]

    #print(loan0.schedule.items())

    schedule = {}

    for loan in loans:
        loan.check_loan_parameters()
        loan.compute_schedule()
        for key, pay in loan.schedule.items():
            if key not in schedule.keys():
                schedule[key] = (key, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
            begin_principal = schedule[key][1] + pay[1]
            payment = schedule[key][2] + pay[2]
            extra_payment = schedule[key][3] + pay[3]
            applied_principal = schedule[key][4] + pay[4]
            applied_interest = schedule[key][5] + pay[5]
            end_principal = schedule[key][6] + pay[6]
            schedule[key] = (key, begin_principal, payment, extra_payment,
                                  applied_principal, applied_interest, end_principal)


    x=[]
    for line in schedule.values():
        content  = list(line)
        a = {'Payment Number': content[0],
                 'Begin Principal': content[1],
                 'Payment': content[2],
                 'Extra Payment': content[3],
                 'Applied Principal': content[4],
                 'Applied Interest': content[5],
                 'End Principal': content[6]}
        x.append(a)
    print(x)




    #x = []

   # for pay in loans.schedule.values():
    #    a = {'Payment Number': pay[0],
     #        'Begin Principal': Helper.display(pay[1]),
      #       'Payment': Helper.display(pay[2]),
       #      'Extra Payment': Helper.display(pay[3]),
        #     'Applied Principal': Helper.display(pay[4]),
         #    'Applied Interest': Helper.display(pay[5]),
          #   'End Principal': Helper.display(pay[6])}
       # x.append(a)
    #print(x)