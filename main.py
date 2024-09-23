""""Main Python script using pandas and matplotlib to read in a csv,
generate summary stats, and create a data visualization."""

from lib.library import (
    generate_summary_stats,
    grab_median,
    generate_sleep_viz,
    generate_study_hours_viz,
)


def summarize():
    """Using the Student Performance csv and summary statistics functions from
    library.py, this function produces summary statistics (mean, median,
    mode, standard deviation, percentiles, max, and min) for each column
    of the dataframe.
    """
    basic_summary = generate_summary_stats()
    median = grab_median()
    return basic_summary, median


def create_visualizations():
    """This function generates scatterplot and histogram visualizations
    of the csv data using
    the respective functions from library.py."""
    generate_study_hours_viz()
    generate_sleep_viz()
