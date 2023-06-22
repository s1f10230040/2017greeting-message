from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        m = 'Good morning'
    elif hour <= 17:
        m = 'Hello'
    else:
        m = 'Good evening'
    message=m + name
    print(message)


greet('Inoue')
