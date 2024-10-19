# README.md Assignment 6

## Task 6.1

### Prerequisites

It is also possible to create a `virtualenv` and install the exact preinstalled packages I have used:

```
pip install -r requirements.txt
```


### Functionality

It creates a Altair plot based on data from the file _owid-covid-data.csv_. 
The chart represents daily new confirmed COVID-19 cases per million people in different countries over time.

The user can specify start date (e.g. "2020-05-10"), end date, and which conutries to include in the chart. 
This is done by including parameters in the function _plot_reported_cases_per_million_.
The paramteres are optional and the defualt start date is 2020-02-24. The deafualt end date is the latest date possible to retreive.
The default countries are the 6 countries that have the highest number of new COVID-19 cases on the end date. 

### Usage

To run the file with the default parameteres, run this command:

``` 
pyhton webvisualization_plot.py  
```

It is possible to change the paramteres in the webcisualization_plot.py file to view plots with different countries and a different time frames. 


## Task 6.2, 6.3 and 6.5

### Prerequisites

It is also possible to create a `virtualenv` and install the exact preinstalled packages I have used:

```
pip install -r requirements.txt
```

### Functionality

With FastApi you can now view a plot of daily new confirmed COVID-19 cases per million people in different countries over time on your local host.
Moreover, the web page has a help menu with information about the functions, and a link to the FastAPI docs. 


### Missing Functionality
 
It is not possible to update the chart with the checkboxes. The checkboxes are visible on the page, but it is not linked to the altair chart. 


### Usage

To display the plots on the web page, run this command: 

``` 
pyhton3 webvisualization.py  
```

Then you have to open the http://127.0.0.1:8000 in your web browser. 
