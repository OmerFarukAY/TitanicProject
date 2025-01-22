import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px


# Loading the Titanic dataset
df = pd.read_csv('titanic.csv')


# Calculating survival rate
df['Survived'] = df['Survived'].map({0: 'No', 1: 'Yes'})


# Survival rate according to Pclass
graph_pclass = px.bar(
    df.groupby('Pclass')['Survived'].value_counts(normalize=True).unstack() * 100,
    barmode='group',
    title='Survival Rate by Passenger Class',
    labels={'value': 'Rate (%)', 'Pclass': 'Passenger Class', 'variable': 'Survival Situation'}
)


# Survival rate by gender
graph_sex = px.histogram(
    df, x='Sex', color='Sex',
    barmode='group',
    title='Survival Rate by Gender',
    labels={'count': 'Number of People', 'Sex': 'Gender'}
)


# Survival rate by age
graph_age = px.histogram(
    df, x='Age', color='Survived',
    nbins=30,
    title='Survival Rate by Age',
    labels={'count': 'Number of People', 'Age': 'Age'}
)


# Creating the Dash app
app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1('Titanic Survival Analysis'),
    dcc.Graph(figure=graph_pclass),
    dcc.Graph(figure=graph_sex),
    dcc.Graph(figure=graph_age)
])


if __name__ == '__main__':
    app.run_server(debug=True)