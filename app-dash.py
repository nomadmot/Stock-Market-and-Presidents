from dash import dcc, html, Dash
from dash.dependencies import Input, Output
from plot_presidents import create_chart

app = Dash(__name__)

value_presidents = "presidents" # selection value for presidents
value_market = "market"         # selection value for markets

app.layout = html.Div(children=[
    html.Title("Dow Market Performance"),
    html.H1("Dow Market Performance by Presidents"),
    dcc.Checklist(              # create a checklist to select chart elements
        id = "select_plots",
        options = [
            {"label": "Show Presidents", "value": value_presidents},
            {"label": "Show Market", "value": value_market}
        ],
        value = [value_presidents, value_market]
    ),
    dcc.Graph(
        id = "chart1"
    )
])

# do the interaction
@app.callback(
    Output(component_id='chart1', component_property='figure'),
    Input(component_id='select_plots', component_property='value')
)

def update_chart(checked_values):
    return create_chart(                    # generate the chart based on selected vales
        value_presidents in checked_values, # "Show Presidents" selected
        value_market in checked_values      # "Show Market" selected
        )

# run the server
if __name__ == '__main__':
	app.run_server(debug=True)