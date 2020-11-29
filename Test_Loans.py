import pytest

from Helper import *
from Loan import *
from LoanImpacts import LoanImpacts
from LoanPortfolio import *

loans = LoanPortfolio()


@pytest.mark.parametrize('principal, rate, term, extra_payment',
                         [
                             (5000.0, 6.0, 24, 0.0),
                             (10000.0, 8.0, 24, 0.0),
                             (7000.0, 7.0, 36, 0.0),
                         ])
def test_loan(principal, rate, term, extra_payment):
    loan = None
    try:
        loan = Loan(principal=principal, rate=rate, term=term, extra_payment=extra_payment)
        loan.check_loan_parameters()
        loan.compute_schedule()
    except ValueError as ex:
        print(ex)
    loans.add_loan(loan)
    Helper.plot(loan)
    Helper.print(loan)

    print(round(loan.total_principal_paid, 2), round(loan.total_interest_paid, 2),
          round(loan.time_to_loan_termination, 0))

    if loans.get_loan_count() == 3:
        loans.aggregate()
        Helper.plot(loans)
        Helper.print(loans)

    assert True


@pytest.mark.parametrize('principal, rate, term, extra_payment, ' +
                         'total_principal_paid, total_interest_paid, time_to_loan_termination',
                         [
                             (27000.0, 4.0, 24, 0.0, 27000.0, 1139.35, 24),
                             (27000.0, 4.0, 24, 25.0, 27000.0, 1115.78, 24)
                         ])
def test_loan_with_extra_payment(principal, rate, term, extra_payment,
                                 total_principal_paid, total_interest_paid,
                                 time_to_loan_termination):
    tolerance_for_cash = 5.0
    tolerance_for_time = 1.0

    loan = None
    try:
        loan = Loan(principal=principal, rate=rate, term=term, extra_payment=extra_payment)
        loan.check_loan_parameters()
        loan.compute_schedule()
    except ValueError as ex:
        print(ex)
    loans.add_loan(loan)
    Helper.plot(loan)

    print(round(loan.total_principal_paid, 2), round(loan.total_interest_paid, 2),
          round(loan.time_to_loan_termination, 0))

    assert abs(loan.total_principal_paid - total_principal_paid) <= tolerance_for_cash
    assert abs(loan.total_interest_paid - total_interest_paid) <= tolerance_for_cash
    assert abs(loan.time_to_loan_termination - time_to_loan_termination) <= tolerance_for_time

    if loans.get_loan_count() == 2:
        loans.aggregate()
        Helper.plot(loans)


@pytest.mark.parametrize('principal, rate, term, extra_payment, contributions',
                         [
                             (68000.0, 4.0, 36, 0, [10, 100, 1000])
                         ])
def test_loan_contribution_1(principal, rate, term, extra_payment, contributions):
    loan_impacts= LoanImpacts(principal=principal, rate=rate, term=term, extra_payment=extra_payment, contributions=contributions)
    loan_impacts.compute_impacts()
    assert True

if __name__ == "__main__":
    pytest.main()