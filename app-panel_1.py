import param
import panel as pn
from panel.interact import interact, interactive, fixed, interact_manual
from panel import widgets as pnw

from plot_presidents import create_chart

# pn.interact(create_chart, presidents=True, market=True).servable()  # the easy way

# set up the selection options
select_presidents = "Show Presidents"
select_market = "Show Market"

# create a Parameterized class for the plot selection
class ChartParms (param.Parameterized):
    selection_list  = param.ListSelector(
        default = [True, True],
        label = [
            "Show Presidents",
            "Show Market"
        ],
        objects = [
            select_presidents,
            select_market
        ]
    )

# create the selection checkbox
selection = pnw.CheckBoxGroup(
    name = "Select Plots",
    options = [
        select_presidents,
        select_market
    ],
    value = [
        select_presidents,
        select_market
    ]
)
# watch the selected values
# selection.param.watch(print, "value")

# helper function to unpack the selected values
def chart_helper(selection):
    return create_chart(
        select_presidents in selection,
        select_market in selection)

# bind the function (there must be a better way)
chart = pn.bind(
    chart_helper,
    selection)

# compose a panel layout
panel = pn.Column(
    "<h1>Dow Jones Performance by President</h1.",
    selection,
    chart
)

# serve the panel
panel.servable( title="Dow Performance")