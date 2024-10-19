"""
Make FastApi of Altair chart over the number of new
COVID-19 cases per million in different countries.
"""

from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from webvisualization_plots import plot_reported_cases_per_million
from webvisualization_plots import get_countries
import webvisualization_plots

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def plot_reported_cases_per_million_html(request: Request):
    """
    Root route for the web application.
    Handle requests that go to the path "/".
    """

    # plot_reported_cases_per_million.html
    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request,
            "countries": webvisualization_plots.get_countries(),
            # further template inputs here
        },
    )


@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(countries: Optional[str] = None):
    """
    Return dict of json chart from altair

    Args:
        countries (list of strings), optional: Countries that you want to
        include in the altair chart.

    Returns:
        dictionary of reported cases per million.
    """
    print(countries)
    if countries:
        countries = countries.split(",")
    fig = plot_reported_cases_per_million(countries, start=None, end=None)

    return fig.to_dict()


@app.get("/help")
def help(request: Request):
    """ Help page that gives information about the different functions """

    # plot_reported_cases_per_million.html
    return templates.TemplateResponse(
        "helpmenu.html",
        {
            "request": request,
        },
    )


def main():
    import uvicorn
    uvicorn.run(app)


if __name__ == "__main__":
    main()
