# this function uses Matplotlib to create a visualization
from helper import market_data
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def mainplot(data):
    # create some font dictionaries 
    fontHeader = {"family":"serif",
                "weight":"extra bold",
                "size": "xx-large"}
    fontSubhead = {"family":"sanserif",
                "weight":"normal",
                "size":"xx-large"}
    fontLabel = {"family":"sanserif",
                "weight":"bold",
                "size":"x-large"}
    fontTick = {"family":"sanserif",
                "weight":"normal",
                "size":"large"}

    # do some initial styling
    #plt.style.use("fivethirtyeight")
    plt.style.use("seaborn-darkgrid")

    # create the figure with a single subplot
    fig, ax1 = plt.subplots(figsize = (20, 25))
    plt.title("Dow Industrial Index Performance by President",
            pad = 20,
            fontdict = fontHeader)

    # create the color map by party affliliation
    colors = ["red" if party == "Republican" else "blue"
            for party in data["Affliliation"]]

    # start with the first president at the top
    ax1.invert_yaxis()

    # create the bar chart
    bars = ax1.barh("President",
                    "Percent Change",
                    data = data,
                    zorder = 1,
                    color = colors)

    # add the "Percent Change" value to the bars
    barLabels = [str(round(value * 100)) + '%'
                for value in bars.datavalues]
    ax1.bar_label(bars,
                labels = barLabels,
                label_type = "edge",
                color = "black",
                fontproperties = fontTick,
                padding = 5,)

    # no need to show the grid, since we put the values on the bars
    ax1.grid(visible = False)

    # add the line plot
    ax2 = ax1.twiny()
    line = ax2.plot("End DOW",
                    "President",
                    '-.Dg',
                    data = data,
                    zorder = 2)

    # send the grid to the back
    ax2.grid(zorder = 0) # why doesn't this work?

    # format the x axis labels
    ax1.set_xlabel("Percent Change",
                labelpad = 15,
                fontdict = fontLabel)
    ax2.set_xlabel("Dow Index Value",
                labelpad = 15,
                fontdict = fontLabel)

    # format the ticks
    ax1.xaxis.set_major_formatter(tick.PercentFormatter(xmax=1))
    ax1.tick_params("x",
                    labelsize = "x-large",
                    pad = 20)
    ax1.tick_params("y",
                    labelsize = "xx-large",
                    pad = 20)

    ax2.tick_params(labelsize = "x-large",
                    pad = 20)

    # set up the legend
    # can't get the handles automatically, need to crate proxies
    red_patch = mpatches.Patch(color='red', label='Republican')
    blue_patch = mpatches.Patch(color='blue', label='Democrat')
    green_line = mlines.Line2D([0,1],[0,0],
                            color ='green',
                            linestyle = '-.',
                            label = "Dow Value")
    # put the legend on ax2 so it come on in front of the gridlines
    ax2.legend(handles=[red_patch, blue_patch, green_line],
            prop = fontTick,
            title = "Legend",
            title_fontproperties = fontHeader,
            frameon = True,
            facecolor = "white",
            edgecolor = "black")

    return fig


def main():
    data = market_data()
    fig = mainplot(data)
    print(fig)
    plt.show()


if __name__ == "__main__":
    main()