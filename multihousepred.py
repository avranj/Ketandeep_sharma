from logging import PlaceHolder
import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from sklearn import linear_model #Here we are declaring it as globally
import math #for using of feature scalling
import csv

#reading csv data
df=pd.read_csv("house_data.csv")
print('for checking data set',df)

#creating object
rg=linear_model.LinearRegression()
rg.fit(df[['Rooms','Distance','Bedroom2','Bathroom','Car','Landsize']],df.Price)
#now callback will handle this from here

app=dash.Dash()

#creating layout main div
app.layout=html.Div([
    #nav wala square
    html.Nav([
        html.H1(id="logo",children="AlphaSolutions.ai"),
        #ul ka div bhi hoga
        html.Ul([html.Li("Home"),html.Li("Source"),html.Li("Contact"),html.Li("Interior"),html.Li("Other"),
        
        ])
        


    ]),

    html.H1(id="ONE",children="-----------PREDICTIVE ANALYSIS-----------"),#children tag will feature as a heading

    #making extradiv for dcc inputs
    html.Div([
        html.H3("Fill All Entries",style={'textAlign':'center','color':'black'}),
        #now giving labels and input so that we can access them
        html.Label("No. of Rooms",style={"fontSize":"18px"}),html.Br(),dcc.Input(type="number",id="i1",value=0),html.Br(),html.Br(),html.Label("Distance",style={'fontsize':'18px'}),html.Br(),dcc.Input(type="number",id="i2",value=0),html.Br(),html.Br(),html.Label("No. of bedrooms",style={'fontsize':'18px'}),html.Br(),dcc.Input(type='number',id="i3",value=0),html.Br(),html.Br(),html.Label("No. of Bathrooms",style={'fontsize':'18px'}),html.Br(),dcc.Input(type="number",id="i4",value=0),html.Br(),html.Br(),html.Label("No. of car garages",style={'fontsize':'18px'}),html.Br(),dcc.Input(type="number",id="i5",value=0),html.Br(),html.Br(),html.Label("Land Size",style={'fontsize':'18px'}),html.Br(),dcc.Input(type="number",id='i6',value=0),
        #dcc.Input(type="number",id="i1",Placeholder="0"),html.Br(),
        #uper hi continue kardiye otherwise print nhi horahe thae

       



    ],id="two"),

    #ek aur div predicted value ko show krne ke liye

     html.Div([
         html.H2("||PROPERTY VALUE||",style={'textAlign':'center','color':'#0c2461'}),html.Br(),html.Br(),
         html.Label(id="ans"),

     ],id="three")




])
#callback part
@app.callback(Output(component_id="ans",component_property="children"),
  [Input(component_id="i1",component_property="value"),
   Input(component_id="i2",component_property="value"),
   Input(component_id="i3",component_property="value"),
   Input(component_id="i4",component_property="value"),
   Input(component_id="i5",component_property="value"),
   Input(component_id="i6",component_property="value"),





])

def prediction(x1,x2,x3,x4,x5,x6):
    L=[int(x1),int(x2),int(x3),int(x4),int(x5),int(x6)]
    print("coefficient",rg.coef_)
    print("intercept",rg.intercept_)
    a=int(rg.predict([L]))
    #a=rg.intercept_ + rg.coef_[0]*L[0] + rg.coef_[1]*L[1] + rg.coef_[2]*L[2] + rg.coef_[3]*L[3] + rg.coef_[4]*L[4] + rg.coef_[5]*L[5]
    print(a)
    return 'predicted value:{}' .format(a)

if __name__ == '__main__':
    app.run_server(debug=True)