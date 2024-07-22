# nuffield-students-exercises

This repository contains exercises for students in the Nuffield Research Placement scheme. 
The exercises are designed to be completed in Python, and are intended to be completed in the order they are presented.

The exercises would not give you a comprehensive understanding of Python, but they should give you a good starting point.
The completion of these exercises is required to be able to work on the project as they cover a lot of the basics that you will need to know.

## Python and Computer Science resources
There are plenty of good resources online to learn how to code in Python. Here are some of the free resources that we recommend:
- Software carpentry introduction to Pyrhon: [Software carpentry](https://swcarpentry.github.io/python-novice-inflammation/01-intro.html)
- Comprehensive intro to computer science: [CS50x](https://cs50.harvard.edu/x/2024/)

You can go through the material before starting the exercises or do them in parallel.

## Specific resources
- [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [What is an environment in Python](https://realpython.com/effective-python-environment/)

## List of the exercises
1. Introduction to Python: print statements, loops, functions
2. Introduction to NumPy: arrays, indexing, slicing, broadcasting
3. From arrays to images: using NumPy to manipulate images and matplotlib to display them

You can find the exercises in the folder `nuffield_students_exercises` and they contain a series of instructions
and questions that you need to answer.

## Setting up your environment
### Install miniconda
In order to complete these exercises, you will need to have Python installed on your computer. We recommend using miniconda, which is a lightweight version of the Anaconda distribution. You can download miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

### Create a new conda environment
Once you have installed miniconda, you can create a new conda environment by running the following command in your terminal:

```bash
conda create --name learn-python python=3.12
```
This will create a new conda environment called `learn-python` with Python 3.12 installed.

### Activate the conda environment
You can activate the conda environment by running the following command in your terminal:

```bash
conda activate learn-python
```

### Install the required packages
You will need to install the required packages to complete the exercises. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Running the exercises
You can run the exercises by running the following command in your terminal:

```bash
python -m nuffield_students_exercises/1_intro_to_python.py
```