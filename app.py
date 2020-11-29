import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd
import plotly.graph_objects as go # or plotly.express as px
import base64
import main
from Helper import *
from contributions import *
from Loan import *
from LoanPortfolio import *
from LoanImpacts import *
from plotly.subplots import make_subplots
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)


# setup app with stylesheets
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Principle Amount"),
                dbc.Input(
                    id='input-principal',
                    placeholder="Type something...",
                    type='float',
                    value=27000,
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Loan term in months"),
                dbc.Input(
                    id='input-term',
                    placeholder="Type something...",
                    type='number',
                    invalid=False,
                    value=24
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Interest rate per year"),
                dbc.Input(
                    id='input-interest',
                    placeholder="Please input interest per year",
                    type='float',
                    value=4
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Extra Payment"),
                dbc.Input(
                    id='input-extra',
                    placeholder="Please input extra payment per month",
                    type='float',
                    value=0
                ),
            ]
        ),

        dbc.Button("Submit", id="Submit-button", outline=True, color="primary", className="mr-1"),
    ],
    body=True, color="light",
)

multi_control_1 = dbc.Card(
    [
        html.H4("Extra Loan 1", className="card-title"),
        dbc.FormGroup(
            [
                dbc.Label("Principle Amount"),
                dbc.Input(
                    id='input-principal-multi1',
                    placeholder="Type something...",
                    type='float',
                    value=27000,
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Loan term in months"),
                dbc.Input(
                    id='input-term-multi1',
                    placeholder="Type something...",
                    type='number',
                    invalid=False,
                    value=24
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Interest rate per year"),
                dbc.Input(
                    id='input-interest-multi1',
                    placeholder="Please input interest per year",
                    type='float',
                    value=4
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Extra Payment"),
                dbc.Input(
                    id='input-extra-multi1',
                    placeholder="Please input extra payment per month",
                    type='float',
                    value=15
                ),
            ]
        ),

        #dbc.Button("Submit", id="Submit-button", outline=True, color="primary", className="mr-1"),
    ],
    body=True, color="light",
)

multi_control_2 = dbc.Card(
    [
        html.H4("Extra Loan 2", className="card-title"),
        dbc.FormGroup(
            [
                dbc.Label("Principle Amount"),
                dbc.Input(
                    id='input-principal-multi2',
                    placeholder="Type something...",
                    type='float',
                    value=10000,
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Loan term in months"),
                dbc.Input(
                    id='input-term-multi2',
                    placeholder="Type something...",
                    type='number',
                    invalid=False,
                    value=24
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Interest rate per year"),
                dbc.Input(
                    id='input-interest-multi2',
                    placeholder="Please input interest per year",
                    type='float',
                    value=4
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Extra Payment"),
                dbc.Input(
                    id='input-extra-multi2',
                    placeholder="Please input extra payment per month",
                    type='float',
                    value=15
                ),
            ]
        ),

        dbc.Button("Submit", id="Submit-button-3", outline=True, color="primary", className="mr-1"),
    ],
    body=True, color="light",
)

table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i}
                 for i in ['Payment Number', 'Begin Principal', 'Payment', 'Extra Payment',
                           'Applied Principal', 'Applied Interest', 'End Principal']],
        style_cell={'textAlign': 'middle',  'width': '7%'},
        style_cell_conditional=[
            {'if': {'column_id': 'Payment Number'},
             'width': '4%'}],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            },
            {
                'if': {'column_id': 'Payment Number'},
                'backgroundColor': 'rgb(248, 248, 248)', 'fontWeight': 'bold'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )

contribution = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Contribution_1"),
                dbc.Input(
                    id='contribution-1',
                    placeholder="Type something...",
                    type='float',
                    value=100,
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Contribution_2"),
                dbc.Input(
                    id='contribution-2',
                    placeholder="Type something...",
                    type='float',
                    value=200,
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Contribution_3"),
                dbc.Input(
                    id='contribution-3',
                    placeholder="Type something...",
                    type='float',
                    value=300,

                ),
            ]
        ),
        dbc.Button("Submit", id="Submit-button-2", outline=True, color="primary", className="mr-1"),
    ],
    body=True, color="light",
)


table_2 = dash_table.DataTable(
    id='table-2',
    columns=[{"name": i, "id": i} for i in
             ['Index','InterestPaid',"Duration",'MIInterest',"MIDuration"]],
    style_cell={'textAlign': 'middle',  'width': '5%'},
    style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            },
            {
                'if': {'column_id': 'Index'},
                'backgroundColor': 'rgb(248, 248, 248)', 'fontWeight': 'bold'
            }
        ],
    style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
)

table_multi = dash_table.DataTable(
        id='table-multi',
        columns=[{"name": i, "id": i}
                 for i in ['Payment Number', 'Begin Principal', 'Payment', 'Extra Payment',
                           'Applied Principal', 'Applied Interest', 'End Principal']],
        style_cell={'textAlign': 'middle',  'width': '7%'},
        style_cell_conditional=[
            {'if': {'column_id': 'Payment Number'},
             'width': '4%'}],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            },
            {
                'if': {'column_id': 'Payment Number'},
                'backgroundColor': 'rgb(248, 248, 248)', 'fontWeight': 'bold'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )

app.layout = dbc.Container(
    [
        dbc.Row(
            [dbc.Col(
                html.H1("Loan Calculator",style={'color':'#4B5658'}),
            )],
            style={'marginTop': 50, 'marginLeft': 40, 'marginRight': 40},
        ),
        dbc.Row(
            [dbc.Col(
                html.H3("Basic Loan", style={'color':'#4B5658'}),
            )],
            style={'marginTop': 80, 'marginBottom': 20, 'marginLeft': 40, 'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="table-graph"), md=8)
            ],
            align="top", style={'marginTop': 20, 'marginLeft': 40,'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(table, md=12),
            ],
            align="Top", style={'marginTop': 30, 'marginBottom': 20, 'marginLeft': 50, 'marginRight': 50},
        ),
        dbc.Row(
            [dbc.Col(
                html.H3("If Your Family Can Help You...", style={'color':'#4B5658'}),
            )],
            style={'marginTop': 80, 'marginBottom': 20, 'marginLeft': 40, 'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(contribution, md=4),
                dbc.Col(table_2, md=8)
            ],
            align="top", style={'marginTop': 20, 'marginLeft': 40,'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="contri-graph-1"), md=6),
                dbc.Col(dcc.Graph(id="contri-graph-2"), md=6)
            ],
            align="top", style={'marginTop': 20, 'marginLeft': 40,'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="contri-graph-3"), md=6),
                dbc.Col(dcc.Graph(id="contri-graph-4"), md=6)
            ],
            align="top", style={'marginTop': 20, 'marginLeft': 40,'marginRight': 40},
        ),
        dbc.Row(
            [dbc.Col(
                html.H3("If Your Have Multiple Loans...", style={'color':'#4B5658'}),
            )],
            style={'marginTop': 80, 'marginBottom': 20, 'marginLeft': 40, 'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(multi_control_1, md=6),
                dbc.Col(multi_control_2, md=6)
            ],
            align="top", style={'marginTop': 20, 'marginLeft': 40,'marginRight': 40},
        ),
        dbc.Row(
            [
                dbc.Col(table_multi, md=12),
            ],
            align="Top", style={'marginTop': 30, 'marginBottom': 20, 'marginLeft': 50, 'marginRight': 50},
        ),
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)


@app.callback(Output('input-principal', 'invalid'),
              Input('input-principal', 'value'))
def check_input_validaty_principal(principal):
    if principal is not None:
        try:
            type(float(principal)) == float
        except:
            return True
        else:
            if float(principal) <= 0.0:
                return True
            else:
                return False
    else:
        return False


@app.callback(Output('input-term', 'invalid'),
              Input('input-term', 'value'))
def check_input_validaty_term(term):
    if term is not None:
        try:
            type(float(term)) == float
        except:
            return True
        else:
            if float(term) <= 0.0:
                return True
            else:
                return False
    else:
        return False


@app.callback(Output('input-interest', 'invalid'),
              Input('input-interest', 'value'))
def check_input_validaty_interest(interest):
    if interest is not None:
        try:
            type(float(interest)) == float
        except:
            return True
        else:
            if float(interest) <= 0.0:
                return True
            else:
                return False
    else:
        return False


@app.callback(Output('input-extra', 'invalid'),
              Input('input-extra', 'value'))
def check_input_validaty_extra(extra):
    if extra is not None:
        try:
            type(float(extra)) == float
        except:
            return True
        else:
            if float(extra) < 0.0:
                return True
            else:
                return False
    else:
        return False

# Draw the table
@app.callback(Output('table','data'),
              Input('Submit-button', 'n_clicks'),
              State('input-principal', 'value'),
              State('input-term', 'value'),
              State('input-interest', 'value'),
              State('input-extra', 'value'))
def loan_calculation(n_clicks,principal,term,interest,extra):
    if n_clicks is not None:
        try:
            loan = Loan(principal=float(principal), rate=float(interest), term=float(term), extra_payment=float(extra))
            loan.check_loan_parameters()
            loan.compute_schedule()
        except ValueError as ex:
            print(ex)

        x = []

        for pay in loan.schedule.values():
            a = {'Payment Number': pay[0],
                 'Begin Principal': Helper.display(pay[1]),
                 'Payment': Helper.display(pay[2]),
                 'Extra Payment': Helper.display(pay[3]),
                 'Applied Principal': Helper.display(pay[4]),
                 'Applied Interest': Helper.display(pay[5]),
                 'End Principal': Helper.display(pay[6])}
            x.append(a)
        return x


@app.callback(
    Output('table-graph', "figure"),
    Input('Submit-button', 'n_clicks'),
    Input('table', "data"))
def update_graph(n_clicks,rows):
    if n_clicks is not None:
        df = pd.DataFrame(rows)
        # Stacked Bar Chart
        index = df.index.tolist()
        x_array = [i+1 for i in index]
        trace_1 = go.Bar(
            x=x_array,
            y=df['Applied Principal'].tolist(),
            name='Principal'
        )

        trace_2 = go.Bar(
            x=x_array,
            y=df['Applied Interest'].tolist(),
            name='Interest'
        )

        trace = [trace_1, trace_2]

        layout = go.Layout(
            title='Amortization Schedule Plot',
            barmode='stack'
        )

        # fig = go.Figure(data=trace, layout=layout)

    else:
        trace = []
        layout = go.Layout(
            title='Amortization Schedule Plot',
            barmode='stack'
        )

    fig = go.Figure(data=trace, layout=layout)
    return fig


# Draw the table of contributions
@app.callback(Output('table-2','data'),
              Input('Submit-button-2', 'n_clicks'),
              State('input-principal', 'value'),
              State('input-term', 'value'),
              State('input-interest', 'value'),
              State('input-extra', 'value'),
              State('contribution-1', 'value'),
              State('contribution-2', 'value'),
              State('contribution-3', 'value'),
              )
def loan_contributions(n_clicks,principal,term,interest,extra,contri_1,contri_2,contri_3):
    if principal is not None and term is not None and interest is not None and extra is not None and \
            contri_1 is not None and contri_2 is not None and contri_3 is not None:
        contri = [float(contri_1), float(contri_2), float(contri_3)]
        df_2 = contribution_of_family(float(principal), float(interest), float(term), float(extra), contri)
        df_2['Index'] = df_2.index
        data = df_2.to_dict('records')
        return data

# draw the graphs of contributions
@app.callback(
    Output('contri-graph-1', "figure"),
    Output('contri-graph-2', "figure"),
    Input('Submit-button-2', 'n_clicks'),
    Input('table-2', "data"))
def update_graph(n_clicks,rows):
    if n_clicks is not None:
        df = pd.DataFrame(rows)

        fig1 = go.Figure()
        x_array = ['-1','0','1','2','3']
        fig1.add_trace(go.Bar(
            x=x_array,
            y=df['InterestPaid'].tolist(),
            name='InterestPaid'
        ))

        fig1.add_trace(go.Scatter(
            x=x_array,
            y=[i*100 for i in df['MIInterest'].tolist()],
            name='MIInterest',
            xaxis='x',
            yaxis='y2'
        ))

        fig1.update_layout(
            title='Contribution of Interest', yaxis2=dict(anchor='x',overlaying='y',side='right')
        )

        labels = ['1', '2', '3']
        values = [i*100 for i in df['MIInterest'].tolist()][2:]
        fig2 = go.Figure()
        fig2.add_trace(go.Pie(labels=labels,values=values))
        fig2.update_layout(
            title='Contribution of Interest by Percentage')


    else:
        trace = []
        layout = go.Layout(
            title='Contribution of Interest',
            barmode='stack'
        )

        fig1 = go.Figure(data=trace, layout=layout)
        fig2 = go.Figure(data=trace, layout=layout)
    return fig1, fig2


@app.callback(
    Output('contri-graph-3', "figure"),
    Output('contri-graph-4', "figure"),
    Input('Submit-button-2', 'n_clicks'),
    Input('table-2', "data"))
def update_graph(n_clicks,rows):
    if n_clicks is not None:
        df = pd.DataFrame(rows)

        fig1 = go.Figure()
        x_array = ['-1','0','1','2','3']
        fig1.add_trace(go.Bar(
            x=x_array,
            y=df['Duration'].tolist(),
            name='Duration'
        ))

        fig1.add_trace(go.Scatter(
            x=x_array,
            y=[i*100 for i in df['MIDuration'].tolist()],
            name='MIDuration',
            xaxis='x',
            yaxis='y2'
        ))

        fig1.update_layout(
            title='Contribution of Duration', yaxis2=dict(anchor='x',overlaying='y',side='right')
        )

        labels = ['1', '2', '3']
        values = [i*100 for i in df['MIDuration'].tolist()][2:]
        fig2 = go.Figure()
        fig2.add_trace(go.Pie(labels=labels,values=values))
        fig2.update_layout(
            title='Contribution of Interest by Percentage')

    else:
        trace = []
        layout = go.Layout(
            title='Contribution of Duration',
            barmode='stack'
        )

        fig1 = go.Figure(data=trace, layout=layout)
        fig2 = go.Figure(data=trace, layout=layout)
    return fig1, fig2


# Table of multiple loans
# Draw the table
@app.callback(Output('table-multi', 'data'),
              Input('Submit-button-3', 'n_clicks'),
              State('input-principal', 'value'),
              State('input-term', 'value'),
              State('input-interest', 'value'),
              State('input-extra', 'value'),
              State('input-principal-multi1', 'value'),
              State('input-term-multi1', 'value'),
              State('input-interest-multi1', 'value'),
              State('input-extra-multi1', 'value'),
              State('input-principal-multi2', 'value'),
              State('input-term-multi2', 'value'),
              State('input-interest-multi2', 'value'),
              State('input-extra-multi2', 'value')
              )
def loan_calculation(n_clicks,principal,term,interest,extra,principal1,term1,interest1,extra1,principal2,term2,interest2,extra2):
    if n_clicks is not None:
        loan0 = Loan(principal=float(principal), rate=float(interest), term=float(term), extra_payment=float(extra))
        loan1 = Loan(principal=float(principal1), rate=float(interest1), term=float(term1), extra_payment=float(extra1))
        loan2 = Loan(principal=float(principal2), rate=float(interest2), term=float(term2), extra_payment=float(extra2))
        loans = [loan0, loan1, loan2]

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

        x = []
        for line in schedule.values():
            content = list(line)
            a = {'Payment Number': content[0],
                 'Begin Principal': round(content[1],2),
                 'Payment': round(content[2],2),
                 'Extra Payment': round(content[3],2),
                 'Applied Principal': round(content[4],2),
                 'Applied Interest': round(content[5],2),
                 'End Principal': round(content[6],2)}
            x.append(a)

        return x

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
