# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('D:\PYTHON\Sales_car.csv')


fig = px.line(df,x='YEAR',y='TATA',title= 'Sales Graph')

app.layout = html.Div([
    html.Div(children=[

        html.H1(children='CAR SALES DATA'),

        html.Div(children='''
        Visualizing with Plotly-dash
        '''),

        html.Br(),
        html.Div(children='''
        Select a brand to see the trend yearwise:
        '''),

        dcc.Dropdown(
            id= 'Brand_selector',
            options = ['MARUTI', 'HYUNDAI', 'KIA', 'FORD', 'TATA'],
            value= 'TATA',
            multi=True
            ),

],style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        dcc.Graph(
        id='Output',
        figure=fig
        )
    ], style={'padding': 10, 'flex': 1})
],style={'display': 'flex', 'flex-direction': 'row', 'background-color': 'rgb(222,184,135)'})

@app.callback(
    Output("Output", "figure"),
    Input("Brand_selector", "value"),
)
def update_output(Input):
    fig = px.line(df, x='YEAR', y=Input, title= 'Sales Graph')
    fig.update_layout(xaxis_title= 'YEAR', yaxis_title= 'No of Cars Sold', template = 'xgridoff')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)






