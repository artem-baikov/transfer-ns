def transfer(num, ns):
    string = ''
    if ns <= 10:
        while num > 0:
            string += str(num % ns)
            num //= ns
        return string[::-1]
    else:
        ns_letts = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17': 'h', '18': 'i',
                    '19': 'j', '20': 'k', '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r',
                    '28': 's', '29': 't', '30': 'u', '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z'}
        lis = []
        while num > 0:
            lis.append(str(num % ns))
            num //= ns
        for n in range(len(lis)):
            if int(lis[n]) >= 10:
                lis[n] = ns_letts[lis[n]]
            string += lis[n]
        return string[::-1]