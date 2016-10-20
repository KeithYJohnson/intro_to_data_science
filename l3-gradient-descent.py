import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it
    # to cost_history.
    # See the Instructor notes for hints.


    sample_size = len(values)
    cost_history = []
    for i in range(num_iterations):
        theta = theta + (alpha/sample_size) * numpy.dot(values - predicted_outcome(features, theta), features)
        cost = compute_cost(features,values,theta)
        cost_history.append(cost)

    return theta, pandas.Series(cost_history) # leave this line for the grader