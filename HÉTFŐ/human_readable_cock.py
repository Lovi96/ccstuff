def make_readable(seconds):
    if seconds == 0:
        return "00:00:00"
    hours = int(seconds / 3600)
    mins = int((seconds - hours * 3600) / 60)
    secs = int(seconds - mins * 60 - hours * 3600)
    h = hours
    m = mins
    s = secs
    if len(str(hours)) == 1:
        h = "0%s" % hours
    if len(str(mins)) == 1:
        m = "0%s" % mins
    if len(str(secs)) == 1:
        s = "0%s" % secs
    return "%s:%s:%s" % (h, m, s)

print(make_readable(86399))
