""" gantt.py;
This program can be used to create a gantt plot using the python plotly library.

The program can be used in different ways, it can be used as an API or as a standalone program.

If the program is run as a standalone program, a JSON file is needed to be able to insert data into the graph.
For this the follow structure should be maintained:
JSON:
[
  {
    "Task": "",
    "Start": "",
    "Finish": "",
    "Resource": ""
  }
]


**
NOTE, THE ORDER OF THE PARTS DOESNT MATTER,
HOWEVER THE GRAPH WILL FOLLOW THE STRUCTURE FOR THE LAYOUT
**
------------------------------
If you are using this program as an API, use the make_gantt function.
This function takes a list of dictionaries with the information needed to make a gantt chart.

To give a dataframe, please use the following format:
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]


"""
__author__ = "Rick Venema"
__version__ = 1.0


import json
import argparse
import plotly.figure_factory as ff


def argparser_gantt():
    """
    This is the argparser of the program, it parses the arguments that are given to it via the commandline.
    IF YOU ARE USING THE PROGRAM AS AN API, DONT USE THIS.
    :return: args, this contains all the arguments that are given via the commandline
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="file",  help="The JSON file that contains the data for the Gantt plot")
    parser.add_argument("-t", dest="title",default="Gantt Plot",
                        help="The title of the gantt plot, defaults to Gantt Plot", nargs="?")
    args = parser.parse_args()
    return args


def make_gantt(data_frame, title="Gantt Plot"):
    """
    This function makes the plot, it takes a data_frame as argument

    :param title: The title that the gantt plot has to use.
    :param data_frame: A data_frame containing the data that has to be plotted in the Gantt Plot
    :return: It shows the Graph that is made with the given data_frame
    """
    fig = ff.create_gantt(data_frame, index_col="Resource", showgrid_x=True, showgrid_y=True, show_colorbar=True,
                          bar_width=0.5, group_tasks=True, title=title)
    # The next lines shows the plot, it opens your standard browser and shows the graph.
    # Using a ssh connection wont work, because a GUI is needed for this function to work
    fig.show()


if __name__ == '__main__':
    arguments = argparser_gantt()
    # Open and load the file needed to make the plot
    json_f = open(arguments.file)
    json_d = json.load(json_f)
    # Makes gantt using the json file given via the commandline
    make_gantt(json_d, title=arguments.title)
