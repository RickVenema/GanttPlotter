# Gantt Plotter
This program can be used to create a gantt plot using the python plotly library.

The program can be used in different ways, it can be used as an API or as a standalone program.

If the program is run as a standalone program, a JSON file is needed to be able to insert data into the graph.
For this the follow structure should be maintained:
JSON:
```json
[
  {
    "Task": "",
    "Start": "",
    "Finish": "",
    "Resource": ""
  }
]
```

**NOTE, THE ORDER OF THE PARTS DOESNT MATTER,
HOWEVER THE GRAPH WILL FOLLOW THE STRUCTURE FOR THE LAYOUT**
------------------------------
If you are using this program as an API, use the make_gantt function.
This function takes a list of dictionaries with the information needed to make a gantt chart.

To give a dataframe, please use the following format:
```python
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
```
