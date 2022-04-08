def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    # YOUR CODE HERE
    return [round(sum(sequence[:i+1])/(i+1), 2) for i, _ in enumerate(sequence)]
    ################

