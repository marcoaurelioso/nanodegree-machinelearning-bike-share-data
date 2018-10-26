# nanodegree-machinelearning-bike-share-data
Machine Learning &amp; AI Foundations Nanodegree - Bike Share Data 

## Explore Chicago Bikeshare Data
### Summary
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.
Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.
In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will use the data from one of the largest cities of United States: Chicago.

### The Datasets
Data for the first six months of 2017 are provided. The data file contain six (6) columns:
* Start Time (e.g. 2017-01-01 00:07:57)
* End Time (e.g. 2017-01-01 00:20:53)
* Trip Duration (in seconds, e.g., 776)
* Start Station (e.g. Broadway & Barry Ave)
* End Station (e.g. Sedgwick St & North Ave)
* User Type (Subscriber or Customer)
* Gender (Male or Female)
* Birth Year (e.g., 1980)

<img src="https://s3.amazonaws.com/video.udacity-data.com/topher/2018/February/5a8107ee_screenshot-2018-02-11-22.20.05/screenshot-2018-02-11-22.20.05.png" alt="Sample bike share data" class="index--image--1wh9w">

### The Questions
You will write code to complete the following tasks:

* Task 1: Print the first 20 samples(rows) from the database
* Task 2: Print the gender(column) of the first 20 samples
* Task 3: Create a function to get the columns as a list
* Task 4: Count how many of each gender do we have
* Task 5: Create a function to count the genders
* Task 6: Show the most popular gender
* Task 7: Plot a a chart using the previous data
* Task 8: Answer why summing the number of Males and Females doesn't match the number of samples
* Task 9: Find the minimum, maximum, mean and median duration of the trips
* Task 10: Get all the start stations of the dataset
* Task 11: Create a function count the occurrence of any given column (optional)

### The Files
To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided as a downloadable .py file. You will also need the dataset file. All of the following files are available for download.
> chicago-bikeshare-us.zip
* bikeshare.py
* chicago.csv

Once you have downloaded this zip file, move to the next page for more details on the code you will be writing.

### How to run the script
You can run the script using a Python integrated development environment (IDE) such as Spyder or Visual Studio Code. To install Spyder, you will need to [download the Anaconda installer](https://www.anaconda.com/download/). This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.
```sh
$ python chicago_bikeshare_pt.py
```

### References
* DictReader - [click here](https://docs.python.org/2/library/csv.html#csv.DictReader)
* Data Structures - [click here](https://docs.python.org/3.6/tutorial/datastructures.html?highlight=data%20list)
* List Comprehensions - [click here](https://docs.python.org/3.6/tutorial/datastructures.html?highlight=data%20list#list-comprehensions)
* Tuples and Sequences - [click here](https://docs.python.org/3.6/tutorial/datastructures.html?highlight=data%20list#tuples-and-sequences)
* Sets - [click here](https://docs.python.org/3.6/tutorial/datastructures.html?highlight=data%20list#sets)
* Math - [click here](https://docs.python.org/3.6/library/math.html?highlight=math%20module#module-math)
