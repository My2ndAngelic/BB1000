def sum_timestamps(l):
    """
    >>> sum_timestamps(['5:32', '4:48'])
    '10:20'
    >>> sum_timestamps(['03:10', '01:00'])
    '4:10'
    >>> sum_timestamps(['2:10', '1:59'])
    '4:09'
    >>> sum_timestamps(['15:32', '45:48'])
    '1:01:20'
    >>> sum_timestamps(['6:15:32', '2:45:48'])
    '9:01:20'
    >>> sum_timestamps(['6:35:32', '2:45:48', '40:10'])
    '10:01:30'
    >>> sum_timestamps(['14:32', '45:48'])
    '1:00:20'
    >>> sum_timestamps(['0:10', '0:20'])
    '0:30'
    """
    # YOUR CODE HERE
    second = 0
    minute = 0
    hour = 0
    for k in [list(reversed(j)) for j in [str.split(i, ':') for i in l]]:
        second = (second + int(k[0]))
        if second > 59:
            second = second % 60
            minute = minute + 1
        minute = (minute + int(k[1]))
        if minute > 59:
            minute = minute % 60
            hour = hour + 1
        if len(k) > 2:
            hour = (hour + int(k[2])) % 60
    return ':'.join(filter(None, [str(hour) if hour > 0 else None,
                                  str(minute).zfill(2) if hour > 0 else str(minute),
                                  str(second).zfill(2)]
                           ))
    ################
