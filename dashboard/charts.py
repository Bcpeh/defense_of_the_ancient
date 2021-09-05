import pandas as pd
pd.options.mode.chained_assignment = None
from common_functions import *
import plotly.graph_objects as go





def radar_layout(fig, selected_hero):
    fig.update_layout(
        title=dict(text=selected_hero, x=0.5,y=0.95),
        polar=dict(
            radialaxis=dict(visible=True, range=[0,1.0]),
            angularaxis=dict(tickfont=dict(size=10), ticks="outside", ticklen=40)
        ),
        width=1200,
        margin=dict(t=150),
        height=900,
        showlegend=True,
        hoverlabel=dict(bgcolor="white", font_size=16),
        hovermode="y unified"
    )
    return fig


def radar_hero_trace(fig,df,selected_hero):
    fig.add_trace(
    go.Scatterpolar(
        r=list(df.loc[selected_hero]),
        theta=df.columns,
        mode='markers+lines',
        text=list(selected_hero),
        textposition="top center",
        textfont_size=15,
        fill="toself",
        fillcolor="#008FD3",
        line=dict(color="#F0AB00"),
        marker=dict(color="#AB7A00",size=5),
        opacity=0.5,
        name=selected_hero
        )
    )

def get_radar_heroes(selected_hero,df):
    fig = go.Figure()
    radar_hero_trace(fig,df,selected_hero)
    fig.update_traces(hovertemplate='%{theta}' + '<br>Value:%{r:.2f}</br>', selector=dict(type='scatterpolar'))
    fig.update_layout(title=dict(text=selected_hero,x=0.5,y=0.95),
                        polar=dict(radialaxis=dict(visible=True,range=[0,1.05]),
                                    angularaxis=dict(tickfont=dict(size=10),ticks="outside",ticklen=40),),
                        width=1200,
                        margin=dict(t=150),
                        height=900,
                        hoverlabel=dict(bgcolor="white",font_size=16),
                        hovermode='y unified')
    return fig