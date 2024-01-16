import altair as alt
import pandas as pd
import pytest

from doeasyeda.create_area_plot import create_area_plot


def test_area_plot_successful_plot_creation():
    """
    Test if the area plot is successfully created with valid input data.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    chart = create_area_plot(df, 'x', 'y')
    assert isinstance(chart, alt.Chart)


def test_area_plot_empty_dataframe():
    """
    Test the area plot creation with an empty DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Empty dataframe received!"):
        create_area_plot(df, 'x', 'y')


def test_area_plot_invalid_column_names():
    """
    Test the area plot creation with invalid column names.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        create_area_plot(df, 'x', 'y')


def test_area_plot_with_width_and_height():
    """
    Test the area plot creation with specified width and height.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    width, height = 400, 300
    chart = create_area_plot(df, 'x', 'y', width=width, height=height)

    chart_dict = chart.to_dict()
    assert chart_dict['width'] == width
    assert chart_dict['height'] == height


def test_area_plot_with_title():
    """
    Test the area plot creation with a specified title.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    title = "Test Area Plot"
    chart = create_area_plot(df, 'x', 'y', title=title)

    chart_dict = chart.to_dict()
    assert chart_dict['title'] == title
