# pml-dl2
Assignment 2 - Movie Recommender System
## Practical Machine Learning and Deep Learning - Assignment 2 - Movie Recommender System

Dinara Yaryeva\
d.yaryeva@innopolis.university\
BS20-RO

## Task:
Your assignment is to create a recommender system of movies for users:
* Your system should suggest some movies to the user based on user's gemographic information(age, gender, occupation, zip code) and favorite movies (list of movie ids).
* Solve this task using a machine learning model. You may consider only one model: it will be enough.
* Create a benchmark that would evaluate the quality of recommendations of your model. Look for commonly used metrics to evaluate a recommender system and use at least one metric.
* Make a single report decribing data exploration, solution implementation, training process, and evaluation on the benchmark.
* Explicitly state the benchmark scores of your systems. 

## Basic usage

### Setup

```bash
git clone https://github.com/dinarayaryeva/pml-dl2.git
```
### Install requirements
```
pip install -r requirements.txt
```

### Evaluate model based on the data

```bash
python benchmark/evaluate.py
```
