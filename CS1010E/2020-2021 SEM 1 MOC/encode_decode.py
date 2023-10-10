def encode_I(word):
    dicta = {}
    lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(lista)):
        dicta[lista[i]] = i
    for i in dicta:
        if len(str(dicta[i])) == 1:
            dicta[i] = '0'+str(dicta[i])
        else:
            dicta[i] = str(dicta[i])
    line = ''
    for i in word:
        if i == ' ':
            line += '99'
        else:
            line += dicta[i]
    return line

def encoding_R(word):
    dicta = {'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04', 'F': '05',
     'G': '06', 'H': '07', 'I': '08', 'J': '09', 'K': '10', 'L': '11',
     'M': '12', 'N': '13', 'O': '14','P': '15', 'Q': '16', 'R': '17',
     'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', ' ': '99'}
    if len(word) == 0:
        return ''
    else:
        return dicta[word[0]] + encoding_R(word[1:])

def decode(msg, offset):
    dicta = {}
    lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lista = lista[-offset%26:]+ lista[:-offset%26]
    for i in range(len(lista)):
        dicta[lista[i]] = i
    for i in dicta:
        if len(str(dicta[i])) == 1:
            dicta[i] = '0'+str(dicta[i])
        else:
            dicta[i] = str(dicta[i])
    dicta[' '] = '99'
    line = ''
    for i in range(0,len(msg)-1,2):
        for j,k in dicta.items():
            if msg[i:i+2] == k:
                line += j
    return line


def decode_with_love(msg):
    for i in range(27):
        dicta = {}
        lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        lista = lista[-i%26:]+ lista[:-i%26]
        for k in range(len(lista)):
            dicta[lista[k]] = k
        for j in dicta:
            if len(str(dicta[j])) == 1:
                dicta[j] = '0'+str(dicta[j])
            else:
                dicta[j] = str(dicta[j])
        dicta[' '] = '99'
        line = ''
        for l in range(0,len(msg)-1,2):
            for j,k in dicta.items():
                if msg[l:l+2] == k:
                    line += j
        if 'LOVE' in line:
            return line

print(decode_with_love('0819199906220299211212119916009919220312'))






















    
