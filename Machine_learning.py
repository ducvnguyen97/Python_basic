'''
1. Data set
    In Machine Learning it is common to work with very large data sets. In this tutorial we will try to make it as easy as possible to understand the different concepts of machine learning, and we will work with small easy-to-understand data sets.
2. Data type
    To analyze data, it is important to know what type of data we are dealing with.

    We can split the data types into three main categories:

        Numerical: data are numbers, and can be split into two numerical categorie
            Discrete data
            Continuous data
        Categorical:data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.
        Ordinal: data are like categorical data, but can be measured up against each other
3. Mean median mode
    In Machine Learning (and in mathematics) there are often three values that interests us:

        Mean - The average value
        Median - The mid point value
        Mode - The most common value
    3.1.Mean
    The mean value is the average value.

    To calculate the mean, find the sum of all values, and divide the sum by the number of values
    The NumPy module has a method for this.
     eg:
        import numpy

        speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

        x = numpy.mean(speed)

        print(x)
    3.2.Median
    The median value is the value in the middle, after you have sorted all the values:
    The NumPy module has a method for this:
     eg:
        import numpy

        import numpy

        speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

        x = numpy.median(speed)

        print(x)
    If there are two numbers in the middle, divide the sum of those numbers by two.
    3.3Mode
    The Mode value is the value that appears the most number of times:
    The SciPy module has a method for this
    eg:
        from scipy import stats

        speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

        x = stats.mode(speed)

        print(x)   
4.Standard Deviation
    4.1. What is Standard Deviation?
        Standard deviation is a number that describes how spread out the values are.

        A low standard deviation means that most of the numbers are close to the mean (average) value.

        A high standard deviation means that the values are spread out over a wider range.
        The NumPy module has a method to calculate the standard deviation
        eg:
            import numpy

            speed = [86,87,88,86,87,85,86]

            x = numpy.std(speed)

            print(x)
    4.2. Variance
        Variance is another number that indicates how spread out the values are.

        In fact, if you take the square root of the variance, you get the standard deviation!

        Or the other way around, if you multiply the standard deviation by itself, you get the variance!
        
        NumPy has a method to calculate the variance:
        eg :
            import numpy

            speed = [32,111,138,28,59,77,97]

            x = numpy.var(speed)

            print(x)
        
        As we have learned, the formula to find the standard deviation is the square root of the variance
    4.3 Symbols
        Standard Deviation is often represented by the symbol Sigma: σ

        Variance is often represented by the symbol Sigma Square: σ2
5. Percentiles
    5.1 What are Percentiles?
      Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
      The NumPy module has a method for finding the specified percentile:
      eg:
        import numpy

        ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

        x = numpy.percentile(ages, 75)

        print(x) 

6. Data Distributtion
    6.1. How Can we Get Big Data Sets?
    To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.    
    eg: Create an array containing 250 random floats between 0 and 5:

        import numpy

        x = numpy.random.uniform(0.0, 5.0, 250)

        print(x)

    6.2. Histogram
        To visualize the data set we can draw a histogram with the data we collected.

        We will use the Python module Matplotlib to draw a histogram.
        eg:
            import numpy
            import matplotlib.pyplot as plt

            x = numpy.random.uniform(0.0, 5.0, 250)

            plt.hist(x, 5)
            plt.show()
    6.3 Big Data Distributions
        An array containing 250 values is not considered very big, but now you know how to create a random set of values, and by changing the parameters, you can create the data set as big as you want.
        eg:
           Create an array with 100000 random numbers, and display them using a histogram with 100 bars:

            import numpy
            import matplotlib.pyplot as plt

            x = numpy.random.uniform(0.0, 5.0, 100000)

            plt.hist(x, 100)
            plt.show()
7. Normal Data Distribution
     In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
        eg:
            import numpy
            import matplotlib.pyplot as plt

            x = numpy.random.normal(5.0, 1.0, 100000)

            plt.hist(x, 100)
            plt.show()
    A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.
    
'''

# Source and Reference: W3School