import dash
from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px
import psycopg2
import time
import warnings
warnings.filterwarnings("ignore")

time.sleep(60)

try: 
    conn = psycopg2.connect(
        database="root_db",
        user="root",
        password="root_pw",
        host="postgresql_container")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weather_table")

    data = cursor.fetchall()

    cursor.close()

    conn.close()

    temp = data[0][1]
    wind = data[0][2]
    description = data[0][3]

except Exception as e:
    print(f"ERROR = {e}")

    temp = "unknown"
    wind = "unknown"
    description = "unknown"

app = dash.Dash()   #initialising dash app
 
app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', 
            children = 'Istanbul', 
            style = {'textAlign':'center', 'marginTop':40,'marginBottom':40}),
    html.H3(id = "H3_1",
           children = f"Temperature = {temp}",
           style= {"textAlign":"center"}),
    html.H3(id = "H3_2",
           children = f"Wind = {wind}",
           style= {"textAlign":"center"}),
    html.H3(id = "H3_3",
           children = f"Description = {description}",
           style= {"textAlign":"center"})
]
                     )
if __name__ == "__main__":
    app.run_server(debug=False, port=8050, host="0.0.0.0")