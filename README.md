# nuffield-students-exercises

This repository contains exercises for students in the Nuffield Research Placement scheme. 
The exercises are designed to be completed in Python, and are intended to be completed in the order they are presented.

The exercises would not give you a comprehensive understanding of Python, but they should give you a good starting point.
The completion of these exercises is required to be able to work on the project as they cover a lot of the basics that you will need to know.

## Python and Computer Science resources
There are plenty of good resources online to learn how to code in Python. Here are some of the free resources that we recommend:
- Software carpentry introduction to Python: [Software carpentry](https://swcarpentry.github.io/python-novice-inflammation/01-intro.html)
- Comprehensive intro to computer science: [CS50x](https://cs50.harvard.edu/x/2024/)
- Learning by examples: [W3Schools](https://www.w3schools.com/python/default.asp)

You can go through the material before starting the exercises or do them in parallel.

## Specific resources
- [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [What is an environment in Python](https://realpython.com/effective-python-environment/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
  
## List of the exercises
1. Introduction to Python: print statements, loops, functions
2. Introduction to NumPy: arrays, indexing, slicing, broadcasting
3. From arrays to images: using NumPy to manipulate images and matplotlib to display them

You can find the exercises in the folder `nuffield_students_exercises` and they contain a series of instructions
and questions that you need to answer.

## Setting up your environment
### Install miniconda
In order to complete these exercises, you will need to have Python installed on your computer. We recommend using miniconda, which is a lightweight version of the Anaconda distribution. You can download miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

> [!NOTE]  
> For Windows users.  
> Download and run the installer from the link above. Make sure to select the option to add miniconda to your PATH. This will allow you to run conda commands from your terminal.  
> If you do not select this option, you will need to add conda to your path. In the start menu, search for "Edit the system environment variables" and click on the button that says "Environment Variables". In the "System variables" section, find the "Path" variable and click on "Edit". Click on "New" and add the path to the miniconda installation directory. This is usually `C:\Users\<your-username>\miniconda3\Scripts` and `C:\Users\<your-username>\miniconda3\Library\bin`.  
> You will need to restart your terminal for the changes to take effect.  
> See also this [tutorial](https://monovm.com/blog/conda-command-not-found-fixed/#:~:text=How%20to%20fix%20Conda%20command%20not%20found%20error%20in%20Windows,Users%5Cusername%5CAnaconda3%5C'.).

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
### Clone the repository
You can clone the repository by running the following command in your terminal:

```bash
git clone https://github.com/neuroinformatics-unit/nuffield-students-exercises.git
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