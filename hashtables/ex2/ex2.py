#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    # Make empty dictionary
    flight_dict = {}
    # Create route variable to store final values
    route = []

    # loop through each ticket
    for i in tickets:
        # set key with ticket source and value with destination
        flight_dict[i.source] = i.destination

    # initialize with destination of 'NONE'
    current_destination = flight_dict["NONE"]

    while current_destination is not "NONE":
        # append current_destination to final route and reassign current_destination
        route.append(current_destination)
        current_destination = flight_dict[current_destination]
    route.append("NONE")

    return route
