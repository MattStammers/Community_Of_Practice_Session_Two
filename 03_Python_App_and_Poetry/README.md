# Python App and Poetry 🤗
Community of Practice Session 2 with UCLH

By Jonny Sheldon, Catalina Carenzo and Matt Stammers

This training takes eda_explosion from [Python_Training_for_BI_Analysts](https://github.com/MattStammers/Python_Training_For_BI_Analysts) and wraps it into Python classes to run in a flask app using poetry.

## Building the App with Poetry

First call:
```sh
poetry install
```

Then call:
```st
poetry shell
```

Then to run the python script call

```sh
cd "03_Python_App_and_Poetry"
python analysis.py
```

To run the flask app make sure you are in the 03_Python_App_and_Poetry

```sh
flask run
```

To run the pytest (see them all pass but please write some more tests as these are rubbish)

```sh
pytest app/test_webapp.py
```

## Challenge

You may notice that the model outputs are slightly different in the webapp than the python notebook. This is because the source data is handled slightly differently in the notebook vs the flask-app.

1. See if you can see where the differences lie and make them match.

2. Then write some tests to check that everything is working as expected.

If you manage this please submit a pull request or email me at matthew.stammers@reallyusefulmodels.com . The first person to fix this feature successfully will get added to the repo.

## Data and Sources

Data Courtesy of: https://www.kaggle.com/datasets/joniarroba/noshowappointments thanks to https://www.kaggle.com/joniarroba

This takes the models found in eda_explosion from [Python_Training_for_BI_Analysts](https://github.com/MattStammers/Python_Training_For_BI_Analysts) and wraps it into Python classes

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
