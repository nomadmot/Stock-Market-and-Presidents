import helper
import plotly.graph_objects as go
from plotly.graph_objs.layout import XAxis

# there doesn't seem to be any way to invert the axes in Plotly, so sort the data instead
data = helper.market_data().sort_values(by = ["Begin Date"], ascending = False)

def create_figure() -> go.Figure:
    # create a layout with 2 x-axes
    layout = go.Layout(
        # basic figure sizes, etc...
        height = 1200,
        width = 1200,
        bargap = 1,
        # the chart title
        title = "Dow Performance by President",
        # formatting for the top x-axis (percent change)
        xaxis = XAxis(
            title = "Percent Change",
            tickformat = '%.1',
            side = 'top'
        ),
        # formatting for the bottom x-axis (dow value)
        xaxis2 = XAxis(
            title = "Dow Value",
            overlaying = 'x', 
            side = 'bottom',
        ),
        # formatting for the y-axis (presidents)... NOTE: no axis title
        yaxis = dict(
            title = ""
        ),
    )
    # now create our figure using the layout created above
    return go.Figure(layout = layout)

def add_chart_presidents(fig: go.Figure):
    # select the republicans aqnd democrats so they can be added with different colors
    # Pandas inserts "NaN" into unselected entries, so Plotly will not add them to the chart
    democrats = data.where(data["Affliliation"] == "Democrat")
    republicans = data.where(data["Affliliation"] == "Republican")

    # the first step is to overlay all the traces onto the figure according to date
    # add a seperate bar trace for each party affliliation so the bars can be color-coded
    fig.add_trace(
        go.Bar(
        y = democrats["Begin Date"],
        x = democrats["Percent Change"],
        name = "Democrat",
        marker_color = 'blue',
        orientation = 'h',
        width = .6))
    fig.add_trace(
        go.Bar(
        y = republicans["Begin Date"],
        x = republicans["Percent Change"],
        name = "Republican",
        marker_color = 'red',
        orientation = 'h',
        width = .6))

     # now that everything is built according to date, it's time to switch the y-axis values over to the president's names
    fig.data[0].y = data["President"]
    fig.data[1].y = data["President"]

    # create a custom hover message
    fig.data[0].hovertemplate = fig.data[1].hovertemplate = "%{label}<br>Percent Change: %{value}"

def add_chart_market(fig: go.Figure):
    # add a line+markers scatter trace showing the Dow Jones value by president
    fig.add_trace(
    go.Scatter(
        y = data["Begin Date"],
        x = data["End DOW"],
        xaxis = 'x2',
        mode = 'lines+markers',
        line_color = 'rgb(0, 128, 0)',
        name= "Dow Index Value",
        orientation = 'h'))

    # now that everything is built according to date, it's time to switch the y-axis values over to the president's names
    fig.data[2].y = data["President"]

    # create a custom hover message
    fig.data[2].hovertemplate = "%{y}<br>Begin Value: %{customdata}<br>End Value: %{x}"


if __name__ == "__main__":
    # display the finished graph
    fig = create_figure()
    add_chart_presidents(fig)
    add_chart_market(fig)
    fig.show()