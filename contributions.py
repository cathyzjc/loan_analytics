import pandas as pd
from Helper import *
from Loan import *
from LoanPortfolio import *
from LoanImpacts import *
import plotly.graph_objects as go


def contribution_of_family(principal,rate,term,extra_payment,contributions):
    loan_all = Loan(principal=float(principal), rate=float(rate),
                            term=float(term), extra_payment=float(extra_payment) + sum(contributions))
    loan_all.check_loan_parameters()
    loan_all.compute_schedule()

    # loan with no contributions (mi)_0
    #
    loan_none = Loan(principal=float(principal), rate=float(rate),
                     term=float(term), extra_payment=float(extra_payment))
    loan_none.check_loan_parameters()
    loan_none.compute_schedule()

    micro_impact_interest_paid_all = \
        (loan_none.total_interest_paid - loan_all.total_interest_paid) / loan_all.total_interest_paid
    micro_impact_duration_all = \
        (loan_none.time_to_loan_termination - loan_all.time_to_loan_termination) / loan_all.time_to_loan_termination

    # micro_impact_interest_paid_all = loan_none.total_interest_paid / loan_all.total_interest_paid
    # micro_impact_duration_all = loan_none.time_to_loan_termination / loan_all.time_to_loan_termination



    all_1 = round(loan_all.total_interest_paid, 2)
    all_2 = loan_all.time_to_loan_termination

    zero_1 = round(loan_none.total_interest_paid, 2)
    zero_2 = loan_none.time_to_loan_termination
    zero_3 = round(micro_impact_interest_paid_all, 4)
    zero_4 = round(micro_impact_duration_all, 4)

    # iterate over each contribution (mi)_index
    #
    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    for index, contribution in enumerate(contributions):
        loan_index = Loan(principal=float(principal), rate=float(rate),
                            term=float(term), extra_payment=float(extra_payment) + sum(contributions) - float(contribution))
        loan_index.check_loan_parameters()
        loan_index.compute_schedule()

        micro_impact_interest_paid = \
            (loan_index.total_interest_paid - loan_all.total_interest_paid) / loan_all.total_interest_paid
        micro_impact_duration = \
            (loan_index.time_to_loan_termination - loan_all.time_to_loan_termination) / loan_all.time_to_loan_termination

        # micro_impact_interest_paid = loan.total_interest_paid / loan_all.total_interest_paid
        # micro_impact_duration = loan.time_to_loan_termination / loan_all.time_to_loan_termination

        line_1.append(round(loan_index.total_interest_paid, 2))
        line_2.append(loan_index.time_to_loan_termination)
        line_3.append(round(micro_impact_interest_paid, 4))
        line_4.append(round(micro_impact_duration, 4))

    data = {'InterestPaid': [all_1,zero_1]+line_1,
                'Duration': [all_2,zero_2]+line_2,
                'MIInterest': ["",zero_3]+line_3,
                'MIDuration':["",zero_4]+line_4
        }

    df = pd.DataFrame(data, index = ['-1','0','1','2','3'], columns = ['InterestPaid',"Duration",'MIInterest',"MIDuration"])
    return df


principal = 27000
interest = 4
term = 12
extra = 15
contri_1 = 100
contri_2 = 100
contri_3 = 100
contri = [float(contri_1), float(contri_2), float(contri_3)]
df = contribution_of_family(float(principal), float(interest), float(term), float(extra), contri)
df['Index'] = df.index
data = df.to_dict('records')



x_array = [-1,0,1,2,3]
trace_1 = go.Bar(
            x=x_array,
            y=df['InterestPaid'].tolist(),
            name='InterestPaid'
        )

trace_2 = go.Scatter(
            x=x_array,
            y=df['MIInterest'].tolist(),
            name='MIInterest',
            mode='lines'
        )

trace = [trace_1, trace_2]

layout = go.Layout(
            title='Contribution',
            #barmode='group'
        )

fig = go.Figure(data=trace, layout=layout)
#fig.show()

