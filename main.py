from urllib.request import urlopen
from urllib.parse import quote
from json import loads
from itertools import groupby


def get_dates(title: str, id: str):
    url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles={quote(title)}'
    data = loads(urlopen(url).read().decode('utf8'))
    dates = []
    for date, repeats in groupby(data['query']['pages'][id]['revisions'], lambda x: x['timestamp'].split('T')[0]):
        dates.append([date, len(list(repeats))])
    dates.sort(key=lambda x: x[1], reverse=True)
    return dates


if __name__ == '__main__':
    grad_dates = get_dates('Градский,_Александр_Борисович', '183903')
    belm_dates = get_dates('Бельмондо,_Жан-Поль', '192203')
    print('Статистика по количеству правок')
    for date in grad_dates:
        print(' '.join([str(x) for x in date]))
    print('\nКорреляция')
    print(belm_dates[0][0])
