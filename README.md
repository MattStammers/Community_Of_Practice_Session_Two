# Community Of Practice Session Two
Community of Practice Session 2 with UCLH

By Matt Stammers🩺, Catalina Carenzo🧪 and Jonny Sheldon🔬

## Session:

There are 4 folders in this repository, each of ascending complexity. Don't worry if you only get to stage 2. The aim is to give you a roadmap to learn docker built on a firm foundation. The four stages are:

1. Documentation with Markdown, Basic Git and Python virtual environments.💖
2. Pipenv and notebooks to perform data science analysis.👏
3. Python apps, classes, poetry and Flask.⚗
4. Containerisation of the app using Docker and production deployment.🤞

## Explainer

- We will explain the file structure during the training. It looks complex but this is necessary to keep you from accidentally comitting secrets to git (even internally) 🐱‍🏍

- The .gitignore file tells git what not to commit to the repository. You should add anything to this you do not want to be committed such as data.🔐

- Ordinarily data would not be committed in a repository at all but as this is a toy/demo app we have done so. Normally, you should add your /data directory to the gitignore file so you don't accidentally commit it to the repo. 🤦‍♂️

- There is also a tool called a pre-commit hook to protect you from accidentally committing sensitive information to git even in metadata. To make sure this is enabled call:

```bat
pre-commit install
```

- Before using git to commit any work. Then the hooks will protect you from accidentally committing a secret. You can add exceptions such as the lockfile or tests to the yaml file with a pipe delimiter 😎 (Yaml is just a heirarhical set of instructions).

## Starting Out

We recommend you start with the folders in order. First get python working and installing basic virtual environments. Then work up the folders gradually. Do not be disheartened if you are only able to get python working slightly at the start - this is a major achievement.🎈

Git allows you to version control your software and roll back any changes you may have made by mistake (or if you break your app).

Virtual Environments (venvs) stop you from ending up with dependency conflicts. There are 3 levels of complexity in venvs:

1. Basic Python venv using a requirements.txt file (great to get started with). The data science alternative is condas but aside from minicondas ([Minicondas](https://docs.anaconda.com/free/miniconda/miniconda-install/)) you now need to pay for the anacondas platform so we would increasingly recommend learning with [Python](https://www.python.org/downloads/) standalone.✨
2. Pipenv which handles everything in one command and is better at avoiding dependency conflicts. It is great for notebooks alone if you don't want to use condas.
3. Poetry which is even more powerful and allows you to deploy fully functional apps so is a better choice for flask.🧨

## Getting There

The key is practice and doing lots of projects. The more you do the better you get.😁

You can use chatGPT or a generative LLM of your choice to help you code. However, you need to make sure you know what the LLM is doing and don't trust it blindly.🧐

Look around online as well on StackOverflow or other sites to find answers to other common questions.😺

Obviously we cannot cover everything in a single 1 hour NHS session but you will find various guides buried within the assets in these folders and we recommend using any helpful resource you find to guide you on your way.😀

## License and Attribution


## Flask

The app can be run as a python script (`python analysis.py`) or as a flask app (`flask run`).

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Data Courtesy of: https://www.kaggle.com/datasets/joniarroba/noshowappointments thanks to https://www.kaggle.com/joniarroba
