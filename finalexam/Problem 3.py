trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(us_num):
    """
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    """
    if len(us_num) == 1 or us_num == '10':
        return trans.get(us_num)
    else:
        if us_num[0] == '1':
            return trans.get('10') + ' ' + trans.get(us_num[1])

        if us_num[1] != '0':
            return trans.get(us_num[0]) + ' ' + trans.get('10') + ' ' + trans.get(us_num[1])
        else:
            return trans.get(us_num[0]) + ' ' + trans.get('10')


print(convert_to_mandarin('36'))  # san shi liu
print(convert_to_mandarin('20'))  # er shi
print(convert_to_mandarin('16'))  # shi liu
print(convert_to_mandarin('10'))  # 'shi'
print(convert_to_mandarin('0'))   # 'ling'
print(convert_to_mandarin('1'))   # 'yi'
