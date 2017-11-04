from datetime import datetime

def getDate():
    now = datetime.now()
    return '{0}{1}{2}'.format(now.year, now.month, now.day)