from lib.library import (
    generate_summary_stats,
    grab_median,
    generate_sleep_viz,
    generate_study_hours_viz,
)


def test_generate_summary_stats():
    """testing out summary stats function"""
    summary = generate_summary_stats()
    medians = grab_median()
    assert summary.loc["mean"]["Hours_Studied"] > 19
    assert medians["Attendance"] == 80.0
    assert summary.loc["std"]["Tutoring_Sessions"] > 1.23


def test_generate_viz():
    """testing out generate viz function"""
    generate_study_hours_viz()
    generate_sleep_viz()


if __name__ == "__main__":
    test_generate_summary_stats()
    test_generate_viz()
