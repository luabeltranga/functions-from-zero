import wikipedia

def scrape(name="microsoft", lenght=1):
    return  wikipedia.summary(name,sentences=lenght)
    