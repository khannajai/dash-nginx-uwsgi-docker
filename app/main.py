import dash
import dash_core_components as dcc
import dash_html_components as html

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server = app, url_base_pathname = '/')

dash_app.css.append_css({"external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background' : '#111111',
    'text' : '#7FDBFF'
}

#Gives the layout of the Dash app
dash_app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "My Dashboard",
                    style={
                        'text-align':'center',
                    }
                ),
            ],
        )
    ],
)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)