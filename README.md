# Community Of Practice Session Two
Community of Practice Session 2 with UCLH

By Matt Stammers, Catalina Carenzo and Jonny Sheldon

# Session:

Data Courtesy of: https://www.kaggle.com/datasets/joniarroba/noshowappointments thanks to https://www.kaggle.com/joniarroba

This takes the models found in eda_explosion from [Python_Training_for_BI_Analysts](https://github.com/MattStammers/Python_Training_For_BI_Analysts) and wraps it into Python classes

## Docker

This code has been wrapped in a docker container and an image of this can be found on [Dockerhub](https://hub.docker.com/repository/docker/ejsheldon/dna_tutorial/general)

To run this:
```bash
docker pull ejsheldon/dna_tutorial:0.0.1
docker run --name dna -p 8000:5000 --rm dna_tutorial:0.0.1
```

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
# Community Of Practice Session Two
Community of Practice Session 2 with UCLH

By Matt Stammers, Catalina Carenzo and Jonny Sheldon


Data Courtesy of: https://www.kaggle.com/datasets/joniarroba/noshowappointments thanks to https://www.kaggle.com/joniarroba

This takes the models found in eda_explosion from [Python_Training_for_BI_Analysts](https://github.com/MattStammers/Python_Training_For_BI_Analysts) and wraps it into Python classes

Shield: [![CC BY 4.0 ][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Learning material: https://www.imperial.ac.uk/students/academic-support/graduate-school/

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://licensebuttons.net/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## Explainer

- We will explain the file structure during the training. It looks complex but this is necessary to keep you from accidentally comitting secrets to git (even internally) 🐱‍🏍

- Ordinarily data would not be committed in a repository but it is necessary for this toy app. Normally, you should add your /data directory to the gitignore file so you don't accidentally commit it to the repo. To make sure this is enabled call:

```bat
pre-commit install
```

before using git to commit any work. Then the hooks will protect you from accidentally committing a secret. You can add exceptions such as the lockfile or tests to the yaml file 😎 (Yaml is just a heirarhical set of instructions).

- Either the Pipenv or requirements.txt files can be used to set up the python environment
