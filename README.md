# doeasyeda

<figure>
    <img src="img/logo2.png" alt="Alt text for image" width="200" height="200">
</figure>

[![ci-cd](https://github.com/UBC-MDS/doeasyeda/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/doeasyeda/actions/workflows/ci-cd.yml) [![Python 3.11+](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-390/) [![codecov](https://codecov.io/gh/UBC-MDS/doeasyeda/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/doeasyeda) [![Documentation Status](https://readthedocs.org/projects/stock_analyzer/badge/?version=latest)](https://doeasyeda.readthedocs.io/en/latest/?badge=latest) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/github/v/release/UBC-MDS/doeasyeda) ![release](https://img.shields.io/github/release-date/UBC-MDS/doeasyeda)

**doeasyeda** offers user-friendly functions for creating standard EDA plots for your data.
---------------------------------------------------------------------------------------

[Installation](#Installation) | [Functions](#Functions) | [Why doeasyeda](#Why-doeasyeda) | [Usage](#Usage)

---

## Project Summary

**doeasyeda** is a Python package designed to streamline the process of Exploratory Data Analysis (EDA) by providing a suite of functions specifically tailored for creating standard EDA plots. This package aims to simplify the visualization aspect of data analysis, making it more accessible and efficient for users.

## Contributors

[Riya Eliza](https://github.com/riyaeliza123), [Hina Bandukwala](https://github.com/hbandukw), [Dan Zhang](https://github.com/wqxxzd) and [Doris Wang](https://github.com/MDSFusionist)

## Installation

```bash
$ pip install doeasyeda
```

## Functions

* **create_hist_plot(df, cols, config=None)** : Generates a histogram plot for specified columns in a DataFrame, with an optional `config` dictionary to customize aspects like chart title, axis labels, and bin sizes, using Altair.
* **create_scatter_plot(df, cols, config=None)** : Creates a scatter plot for chosen DataFrame columns, allowing customization through an optional `config` parameter for setting chart title, axis labels, and color schemes, rendered using Altair.
* **create_line_plot(df, cols, config=None)** : Develops a line plot using selected columns in a DataFrame, featuring an optional `config` parameter to customize the plot's appearance, including chart title, axis labels, and color schemes, using Altair.
* **create_area_plot(df, cols, config=None)** : Produces an area plot for designated columns in a DataFrame, with an optional `config` for detailed plot customization such as chart title, axis labels, and color schemes, visualized using Altair.

## Why doeasyeda?

**doeasyeda** positions itself as a valuable addition to the Python ecosystem, particularly in the realm of data visualization and EDA. While it shares its fundamental objective with existing packages like [pandas-profiling](https://github.com/ydataai/ydata-profiling) and [Dtale](https://pypi.org/project/dtale/), which provides comprehensive EDA reports with a single line of code, **doeasyeda** differentiates itself by focusing on customizable, individual plot generation. While pandas-profing is excellent for generating automated detailed reports on entire datasets, Dtale integrates advanced libraries like Plotly and Seaborn , **doeasyeda** allows users more control and flexibility in visualizing specific aspects of their data through its range of plotting functions from altair library. **doeasyeda** has the following key features:

* **User-Friendly** : **doeasyeda** is built with simplicity in mind. The functions are easy to use, allowing users to generate insightful plots with minimal coding effort.
* **Versatile Plotting Functions** : The package includes a variety of plotting functions, each tailored to display data effectively. These functions cater to different data types and visualization needs.
* **Focus on Standard EDA Plots** : The package emphasizes standard EDA plots, ensuring that users can cover the fundamental aspects of data visualization in their analysis.

## Dependencies

## Usage

Our package primarily utilizes the gapminder dataset to demonstrate the effectiveness and versatility of our plotting functions. However, the functions within **doeasyeda** are designed to be flexible and can be applied to a wide range of datasets, making this package a valuable tool for any data scientist or analyst looking to conduct comprehensive EDA.

Below is a simple quick start example:

## Documentation

Online documentation can be found [here]().

Publishing on [TestPyPi]() and [PyPi]().

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`doeasyeda` was created by Riya Eliza, Hina Bandukwala, Dan Zhang and Doris Wang. It is licensed under the terms of the MIT license.

## Credits

`doeasyeda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
