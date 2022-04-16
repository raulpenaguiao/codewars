def format_duration(seconds):
    if seconds == 0:
        return "now"
    sec = seconds%60
    minutes = (seconds//60)%60
    hours = (seconds//3600)%24
    days = (seconds//86400)%365
    years = (seconds//31536000)
    sections = []
    if years > 1:
        sections.append(str(years) + " years")
    if years == 1:
        sections.append(str(years) + " year")
    if days > 1:
        sections.append(str(days) + " days")
    if days == 1:
        sections.append(str(days) + " day")
    if hours > 1:
        sections.append(str(hours) + " hours")
    if hours == 1:
        sections.append(str(hours) + " hour")
    if minutes > 1:
        sections.append(str(minutes) + " minutes")
    if minutes == 1:
        sections.append(str(minutes) + " minute")
    if sec > 1:
        sections.append(str(sec) + " seconds")
    if sec == 1:
        sections.append(str(sec) + " second")
    if len(sections) == 1:
        return sections[0]
    s = ", ".join(sections[:-1])
    return s + " and " + sections[-1]
    #your code here
