import app_panel_1 as panel
from flask import Flask

# define Flask app parameters
title = "Presidential Dow Performance"
app = Flask(__name__,)

# serve the panel
@app.route('/')
def show_panel(panel):
    panel.show(title=title)

show_panel(panel.panel)