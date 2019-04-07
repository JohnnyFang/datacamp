'''
Creating rows of plots

Layouts are collections of Bokeh figure objects.

In this exercise, you're going to create two plots from the Literacy and Birth Rate data set to plot fertility vs female literacy and population vs female literacy.

By using the row() method, you'll create a single layout of the two figures.

Remember, as in the previous chapter, once you have created your figures, you can interact with them in various ways.

In this exercise, you may have to scroll sideways to view both figures in the row layout. Alternatively, you can view the figures in a new window by clicking on the expand icon to the right of the "Bokeh plot" tab.

Instructions

    Import row from the bokeh.layouts module.
    Create a new figure p1 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
    Add a circle glyph to p1. The x-axis data is fertility and y-axis data is female_literacy. Be sure to also specify source=source.
    Create a new figure p2 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
    Add a circle() glyph to p2, specifying the x and y parameters.
    Put p1 and p2 into a horizontal layout using row().
    Click 'Submit Answer' to output the file and show the figure.
'''
