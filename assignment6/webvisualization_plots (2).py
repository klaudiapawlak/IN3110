"""
Creates a plot based on corona dataset from the following website:
https://ourworldindata.org/covid-cases

"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as pl
import altair as alt
from datetime import datetime


def get_data_from_csv(column, countries=None, start="2020-02-24", end=None):
    """
    Creates pandas dataframe from .csv file. Data will be filtered based on
    data column name, list of countries to be plotted and time frame chosen.

    Args:
        column (string): the data column you want to include
        countries ((list(string), optional): List of countries you want to
                                             include. If none is passed,
                                             dataframe should be filtered for
                                             the 6 countries with the highest
                                             number of cases per million at the
                                             last current date available in the
                                             timeframe chosen.
        start (string, optional): The first date to include in the returned
                                  dataframe. If specified, records earlier than
                                  this will be excluded. Default: the earliest
                                  date "2021-10-10".
        end (string, optional): The latest date to include in the returned data
                                frame. If specified, records later than this
                                will be excluded. Example format: "2021-10-10".

    Returns:
        cases_df (dataframe): returns dataframe for the timeframe, columns,
                              and countries chosen.
    """

    # add path to .csv file from 6.0
    path = column

    # read .csv file, define which columns to read
    df = pd.read_csv(
        path,
        sep=",",
        usecols=["location"] + ["date"] + ["new_cases_per_million"],
        parse_dates=["date"],
        date_parser=lambda col: pd.to_datetime(col, format="%Y-%m-%d"),
    )

    if countries is None:
        # no countries specified, pick 6 countries with the highest case
        # count at end_date
        if end is None:
            # no end date specified, pick latest date available
            end_date = df.date.iloc[-1]
        else:
            end_date = datetime.strptime(end, "%Y-%m-%d")
        df_latest_dates = df[df.date.isin([end_date])]
        # identify the 6 countries with the highest case count
        # on the last included day
        sorted_df = df_latest_dates.sort_values(by=["new_cases_per_million"],
                                                ascending=False).head(6)
        countries = sorted_df["location"].values.tolist()

    # now filter to include only the selected countries
    cases_df = df[df["location"].isin(countries)]
    # print(cases_df)
    # apply date filters
    if start:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        # exclude records earlier than start_date
        mask = (cases_df["date"] >= start_date)
        cases_df = cases_df.loc[mask]

    if end:
        end_date = datetime.strptime(end, "%Y-%m-%d")
        if start_date and start_date >= end_date:
            raise ValueError("The start date must be earlier " +
                             "than the end date.")

        # exclude records later than end date
        mask = (cases_df["date"] <= end_date)
        cases_df = cases_df.loc[mask]

    return cases_df


def get_countries():
    """
    Returns all the unique countries from the csv file "owid-covid-data"

    Returns:
        countries (numpy array) with all thw unique countries

    """
    df = pd.read_csv("owid-covid-data.csv")
    # cases_df = get_data_from_csv("owid-covid-data.csv")
    countries = df.location.unique()
    return countries

# get_data_from_csv(start="2021-11-14")


def plot_reported_cases_per_million(countries=None, start=None, end=None):
    """
    Plots data of reported covid-19 cases per million using altair.
    Calls the function get_data_from_csv to receive a dataframe used for
    plotting.

    Args:
        countries ((list(string), optional): List of countries you want to
                                             filter. If none is passed,
                                             dataframe will be filtered for the
                                             6 countries with the highest
                                             number of cases per million at the
                                             last current date available in the
                                             timeframe chosen.
        start (string, optional): a string of the start date of the table, none
                                  of the dates will be older then this on.
        end (string, optional): a string of the en date of the table, none of
                                the dates will be newer then this one.

    Returns:
        altair Chart of number of reported covid-19 cases over time.
    """

    # choose data column to be extracted
    column = "owid-covid-data.csv"
    # create dataframe
    cases_df = get_data_from_csv(column, countries=countries,
                                 start=start, end=end)

    # Note: when you want to plot all countries simultaneously while enabling
    # checkboxes, you might need to disable altairs max row limit by commenting
    # in the following line
    alt.data_transformers.disable_max_rows()

    chart = (
        alt.Chart(cases_df,
                  title="Daily new confirmed COVID-19 " +
                        "cases per million people")
        .mark_line()
        .encode(
            x=alt.X(
                "date:T",
                axis=alt.Axis(
                    format="%d, %b, %Y",
                    title="Date",
                    titleFontSize=14,
                    tickCount=20
                ),
            ),
            y=alt.Y(
                "new_cases_per_million",
                axis=alt.Axis(
                    title="Number of Reported Cases per Million",
                    titleFontSize=14,
                    tickCount=10,
                ),
            ),
            color=alt.Color("location:N", legend=alt.Legend(title="Country")),
        )
        .interactive()
    )
    return chart


def main():
    """Function called when run as a script
    Creates a chart and display it or save it to a file
    """
    chart = plot_reported_cases_per_million()
    chart.show()


if __name__ == "__main__":
    main()
