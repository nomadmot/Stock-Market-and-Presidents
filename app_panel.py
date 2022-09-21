import param
import panel as pn
from panel.interact import interact, interactive, fixed, interact_manual
from panel import widgets as pnw

from plot_presidents import create_chart

# pn.interact(create_chart, presidents=True, market=True).servable()  # the easy way

# create a Parameterized class for the plot selection
class ChartParms (param.Parameterized):
    select_presidents = param.Boolean(True, label = "Show Presidents")
    select_market = param.Boolean(True, label = "Show Market")

    # link the chart
    @param.depends(
        "select_presidents", 
        "select_market"
        )
    def call_chart(self):
        return create_chart(
            self.select_presidents, 
            self.select_market
            )

# compose a panel layout
parms = ChartParms( name = "Chart Selections:")
panel = pn.Column(
    "<h1>Dow Jones Performance by President</h1.",
    parms.param,
    parms.call_chart
)


# serve the panel
panel.servable( title="Dow Performance")