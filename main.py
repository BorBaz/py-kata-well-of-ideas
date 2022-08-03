# Mine
def well(x):
    occurrences = x.count('good')

    result = 'Fail!'

    if occurrences > 0 and occurrences < 3:
        result = 'Publish!'
    elif occurrences > 2:
        result = 'I smell a series!'

    return result

# Best
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


print(well(['good', 'good', 'good']))
