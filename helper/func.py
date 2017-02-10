from random import randint

def unique_csv(text, folder):
    random = str(randint(0, 100) * randint(0, 100))
    id = '-sentiment-{0}'.format(random)
    folder = './{0}/'.format(folder)
    return folder + text + id + '.csv'
