from re import S
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from charts import *

app = dash.Dash(__name__, external_stylesheets=["./assets/main_stylesheet.css"])
df = pd.read_csv('./downloads/hero_data/hero_stats_23August2021.csv')
hero_list, df = preprocess_df(df)
# app.layout = html.Div([
#     html.Div(
#         children=[
#             html.H1("Defense of the Ancient (DOTA2)", style={"padding":0, "margin": 0},),
#             html.Div(id="content", children=[], className="vertical-middle"),
#             ],
#             className="verticle-middle",
#         ),
#     ]
# )

app.layout = html.Div([
        html.H1("Defense of the Ancient (DOTA2)", style={"padding":0, "margin": 0},),
        dcc.Dropdown(
            id='hero_chosen',
            options=[{"label": i, 'value': i} for i in hero_list],
            value='Anti-Mage'
        ), dcc.Graph(id='radar_chart')])

@app.callback(
    Output("radar_chart", "figure"),[Input("hero_chosen","value")])
def getting_demo_data(selected_hero):
    radar_chart = get_radar_heroes(selected_hero,df)
    # child = [
    #     # dcc.Dropdown(
    #     #     {"id":"selected_hero"},
    #     #     value=selected_hero,
    #     #     options=hero_list,
    #     #     style={"minWidth": "250px",}
    #     # ),
    #     dcc.Graph({"id":"heroes_radar"}, figure=radar_chart,responsive=True,className="graphs"),
    # ]
    return radar_chart

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=2810, use_reloader=False)