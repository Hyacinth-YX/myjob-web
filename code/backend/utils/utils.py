def salary_parse(string: str):
    if string is None:
        return 0
    if string.find('13薪') > -1:
        ratio = 13
    elif string.find('/天') > -1:
        ratio = 256
    elif string.find('/时') > -1:
        ratio = 8*256
    else:
        ratio = 12
    if string.find('K') > -1:
        ratio *= 1000
    string = string.split('元')[0].split('K')[0]
    min_num, max_num = list(
        map(lambda x: int(float(x.strip())), string.split('-')[:2]))
    return (min_num+max_num)/2*ratio
