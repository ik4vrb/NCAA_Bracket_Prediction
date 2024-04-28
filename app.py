import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import json
import plotly.graph_objs as go

# Load team probabilities from the JSON file
with open('team_probabilities.json', 'r') as f:
    team_probabilities = json.load(f)

# load the CSS stylesheet
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Define the Dash application
app = dash.Dash(__name__, external_stylesheets=stylesheets)
server = app.server

# Define dropdown options for team selection
team_options = [{'label': team, 'value': team} for team in team_probabilities.keys()]

# Define layout of the dashboard
app.layout = html.Div([
    html.H1("NCAA Tournament Probability Dashboard"),
    html.Div([
        html.Label('Select Team 1:'),
        dcc.Dropdown(
            id='team-dropdown-1',
            options=team_options,
            value=team_options[0]['value'],  # Default value
            multi=False,
            searchable=True,
            placeholder="Select a team"
        ),
        html.Label('Select Team 2:'),
        dcc.Dropdown(
            id='team-dropdown-2',
            options=team_options,
            value=team_options[1]['value'],  # Default value
            multi=False,
            searchable=True,
            placeholder="Select a team"
        ),
    ]),
    dcc.Graph(id='probability-bar-chart'),
    html.Div([
        dcc.Graph(id='probability-pie-chart-1')
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='probability-pie-chart-2')
    ], style={'width': '49%', 'display': 'inline-block'})
])

# Define callback to update probability charts based on team selection
@app.callback(
    [Output('probability-bar-chart', 'figure'),
     Output('probability-pie-chart-1', 'figure'),
     Output('probability-pie-chart-2', 'figure')],
    [Input('team-dropdown-1', 'value'),
     Input('team-dropdown-2', 'value')]
)
def update_probability_charts(selected_team_1, selected_team_2):
    # Get probabilities for the selected teams from the loaded data
    probabilities_1 = team_probabilities.get(selected_team_1, {})
    probabilities_2 = team_probabilities.get(selected_team_2, {})
    
    # Create data for the bar chart
    bar_chart_data = [
        go.Bar(
            x=list(probabilities_1.keys()),
            y=list(probabilities_1.values()),
            name=selected_team_1,
            marker=dict(color='blue')
        ),
        go.Bar(
            x=list(probabilities_2.keys()),
            y=list(probabilities_2.values()),
            name=selected_team_2,
            marker=dict(color='red')
        )
    ]
    bar_chart_layout = go.Layout(
        title='Probabilities by Round (Bar Chart)',
        xaxis=dict(title='Tournament Round'),
        yaxis=dict(title='Probability')
    )
    
    # Create data for the pie charts
    pie_chart_data_1 = [
        go.Pie(
            labels=list(probabilities_1.keys()),
            values=list(probabilities_1.values()),
            name=selected_team_1
        )
    ]
    pie_chart_data_2 = [
        go.Pie(
            labels=list(probabilities_2.keys()),
            values=list(probabilities_2.values()),
            name=selected_team_2
        )
    ]
    pie_chart_layout = go.Layout(
        title=f'Probabilities by Round (Pie Chart) - {selected_team_1}',
        width=400,
        height=400
    )
    
    pie_chart_layout_2 = go.Layout(
        title=f'Probabilities by Round (Pie Chart) - {selected_team_2}',
        width=400,
        height=400
    )
    
    return {'data': bar_chart_data, 'layout': bar_chart_layout}, {'data': pie_chart_data_1, 'layout': pie_chart_layout}, {'data': pie_chart_data_2, 'layout': pie_chart_layout_2}

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
