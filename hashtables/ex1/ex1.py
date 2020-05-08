def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create a dictionary for weights
    weights_dict = {}

    # loop to check if key value pair already in weights_dict
    for i in range(length):
        diff = limit - weights[i]

        # if already in weights_dict
        if weights_dict.get(diff) is not None:
            # return i and retrieve diff
            return (i, weights_dict.get(diff))
        else:
            # set key as with current value and value with index
            weights_dict[weights[i]] = i

    return None
