# Project : Logs Analysis

## Purpose

This project is part of the [Udacity Full Stack Web Development Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) program. The project allows students to flex their SQL database skills as well as interact with a large database with over a million rows. The project also imitates real world scenarios in which a developer may need to generate informative reports using logs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

* [Python3](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Setup
1. Install Vagrant, VirtualBox, and Python3. Installation instructions can be found using the links above.
2. Clone or Fork this repository

### To Run

Once installed, launch Vagrant VM by running `vagrant up`, and logging in with `vagrant ssh`

To load the database, use the command `psql -d news -f newsdata.sql`. This will allow you to connect to the database and run the necessary SQL statements.

To execute the program, run `python3 newsdata.py`

#### The Database
The database includes three tables :
* Authors - contains article author names, a bio, and ID
* Articles - contains information about the article, including a Title and Body, as well as a foreign key referencing Author ID
* Log - contains a single record for every time the website was accessed. This record contains the path accessed, status, method, etc....

### Coding style
The code conforms to the PEP8 style recommendations.

Install the following and run against code to test style recommendations:
`pip install pycodestyle` or `pip3 install pycodestyle`
Run using `pycodestyle`

## Authors

* **Justin Cook**

## Acknowledgments

* Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code, 1/e By: Zed A. Shaw
* https://www.postgresql.org/docs/9.1/static/queries-with.html
* https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
