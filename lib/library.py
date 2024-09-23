"""Library file that contains shared functions 
for main.py script and Jupyter notebook."""

import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """This function loads the StudentPerformanceFactors.csv file 
    into a pandas dataframe
    and returns it."""
    data_frame = pd.read_csv("StudentPerformanceFactors.csv")
    return data_frame


def generate_summary_stats():
    """Using the Performance csv file, this function generates summary statistics (mean,
    mode, standard deviation, as well as percentiles) for each column of the dataframe
    using the pandas describe method.
    """
    data_frame = load_data()
    return data_frame.describe()

def grab_max():
    """Returns maximum values of all of the numeric columns of the provided csv file."""
    data_frame = load_data()
    return data_frame.max(numeric_only=True)

def grab_median():
    """Returns median values of all of the numeric columns of the provided csv file."""
    data_frame = load_data()
    return data_frame.median(numeric_only=True)

def grab_min():
    """Returns maximum values of all of the numeric columns of the provided csv file."""
    data_frame = load_data()
    return data_frame.min(numeric_only=True)

def generate_study_hours_viz():
    """This function generates a scatter plot visualization 
    of hours studied vs. exam scores
    from the Student Performance dataset."""
    data_frame = load_data()
    plt.scatter(data_frame["Hours_Studied"], data_frame["Exam_Score"], color="Green")
    plt.xlabel("Hours Studied")
    plt.ylabel("Student Exam Scores")
    plt.title("Relationship Between Hours Studied and Student Exam Scores")
    plt.savefig("hours_studied_performance.png")
    plt.show()

def generate_sleep_viz():
    """This function generates a histogram visualization of student sleep hours
    from the Student Performance dataset."""
    data_frame = load_data()
    plt.hist(data_frame["Sleep_Hours"], color="Blue")
    plt.xlabel("Hours Slept")
    plt.title("Hours Slept by Students")
    plt.savefig("sleep_performance.png")
    plt.show()

print(grab_median())

