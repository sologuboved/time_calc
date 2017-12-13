def process_date_ouput(output, delta):
    if delta:
        output = output.days
        if output == 1:
            inflection = ''
        else:
            inflection = 's'
        return "%d day%s" % (output, inflection)

    return output.strftime("%d %B %Y, %A")


def process_time_output(output, with_days):
    if with_days:
        hrs, mins, secs = output
        return "%d:%d:%d" % (hrs, mins, secs)

    hrs, mins, secs = output
    return "%d:%d.%d" % (hrs, mins, secs)