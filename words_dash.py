import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import words

# Read in dataframe of each domain name and the words within each one, from test_df.py
#df = pd.read_csv('/Users/lissacallahan/Python/domain_names/words_dataframe.csv')
domains = ["examplecartrading.com", "examplepensions.co.uk", "exampledeals.org", "examplesummeroffers.com"]
df = words.by_domain(domains)

df.to_csv (r'/Users/lissacallahan/Python/domain_names/words_dataframe.csv', header=True)
df = pd.read_csv('/Users/lissacallahan/Python/domain_names/words_dataframe.csv')

print(df)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)