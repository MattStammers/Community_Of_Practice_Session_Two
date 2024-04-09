# Dockerisation 👀
Community of Practice Session 2 with UCLH

By Matt Stammers, Catalina Carenzo and Jonny Sheldon

# Session:

Data Courtesy of: https://www.kaggle.com/datasets/joniarroba/noshowappointments thanks to https://www.kaggle.com/joniarroba

This takes the models found in eda_explosion from [Python_Training_for_BI_Analysts](https://github.com/MattStammers/Python_Training_For_BI_Analysts) and wraps it into Python classes

## Docker

This code has been wrapped in a docker container and an image of this can be found on [Dockerhub](https://hub.docker.com/repository/docker/ejsheldon/dna_tutorial/general)

To run this install docker and WSL then run the above or cd to the 04_Containerised_App folder and run:

```sh
docker docker build -t no_shows_improved .
docker docker run -d -p 5000:5000 no_shows_improved
```

Now if you navigate to localhost:5000 in any browser the app should be up in the container.

To kill all the containers and start again

```sh
docker stop $(docker ps -aq)
```

Then run the container again to start it up once more.

## Enjoy! 😁

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
