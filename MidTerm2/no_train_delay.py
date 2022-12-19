# Given a schedule containing arrival and departure time of trains in a station.
arrival = [1.00, 1.10, 2.00, 2.20, 2.50, 4.00]
departure = [1.30, 2.40, 2.20, 3.30, 3.00, 4.20]

output = "Minimum platform needed is 2"


def validate_input(arrival: list, departure: list) -> bool:
    """
    Validate the input
    :param arrival: list of arrival times
    :param departure: list of departure times
    :return: True if valid, False otherwise
    """
    # check if the arrival and departure times are of the same length
    if len(arrival) != len(departure):
        return False
    for i in range(len(arrival)):
        # check if the type of inputs are valid
        if not isinstance(arrival[i], (int, float)) or not isinstance(departure[i], (int, float)):
            return False
        # check if the arrival and departure times are valid
        if arrival[i] >= departure[i]:
            return False
    return True


def format_answer(num: int) -> str:
    return f"Minimum platform needed is {num}"


def find_number_of_platforms(arrival: list, departure: list) -> int:
    """
    Find the minimum number of platforms required for the station so that no train waits.
    :param arrival: list of arrival times
    :param departure: list of departure times
    :return: number of platforms
    """
    # sort arrival and departure times
    arrival.sort()
    departure.sort()

    # initialize the number of platforms
    platforms = 1
    max_platforms = 1

    # initialize the index of arrival and departure
    i = 1
    j = 0

    # iterate over the arrival and departure times
    while i < len(arrival) and j < len(departure):
        # if the arrival time is less than the departure time
        if arrival[i] < departure[j]:
            # increment the number of platforms
            platforms += 1
            # increment the index of arrival
            i += 1
        # if the arrival time is greater than the departure time
        else:
            # decrement the number of platforms
            platforms -= 1
            # increment the index of departure
            j += 1

        # update the maximum number of platforms
        max_platforms = max(max_platforms, platforms)

    return max_platforms


if __name__ == '__main__':
    # validate the inputs
    assert validate_input(arrival, departure), 'Invalid input'

    # find the minimum number of platforms
    min_n_of_platforms = find_number_of_platforms(arrival, departure)

    _output = format_answer(min_n_of_platforms)
    print(_output)
