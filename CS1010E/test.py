def decipher_message(msg,guide):
    message = ''
    for i in msg:
        if i not in guide.keys():
            message += i
        else:
            message += guide[i]
    return message

def decode_map(mapfile,ddict,outfile):
    with open(mapfile, 'r') as f:
        file = f.readlines()
    message = decipher_message(''.join(file), ddict)
    with open(outfile, 'w') as f:
        f.write(message)

def find_treasure(mapfile):
    new_file = 'en' + mapfile[2:]
    decode_map(new_file,ddict,mapfile)
    with open(mapfile, 'r') as f:
        decoded = f.readlines()
    for i in range(1,len(decoded)-1):
        for k in range(1,len(decoded[i])-1):
            if decoded[i][k-1] + decoded[i][k] + decoded[i][k+1] == 'TTT' and decoded[i-1][k] == 'T' and decoded[i+1][k] == 'T':
                return (i,k)

with open('encoded_map2.txt','w') as f:
    f.write('1DDDDZZ1DDDZZ1DD1ZD11ZD2FFC20BB++0401D11Z1D1\nDD11DDZDDDDZ11DD1D1ZZZ224C00;;B;0040ZDDZ1ZZ1\nD1ZZZ1ZZ111D111ZD1Z1Z1000222+;;040404Z1DDDZD\nZ11ZZ11DDD1DDZ1ZDDD1D22C42044++;;0030Z11D1ZD\n1DDD1111DZZDZ1D1D11ZZ20202220B;+B40F4ZDD1D1D\nD1ZD111ZDD1DDZ1Z1ZZD42044044BB+4420F0DZZ1ZZD\nZDZDZD1DDD1ZDD11ZD1Z04444440+B;2400441Z11ZZZ\nZDDD111ZZZZZZDZDZZZ11Z00200;+;+44040Z1DZ111D\n11Z1D1ZDD1ZD1D1Z11ZDZD04220+BB224240DDZ111D1\nDZ1ZDDDD1D1ZZ1ZDDDZZ1114442;B240442D1DZ11Z11\nZZZDD1Z1D1Z1ZD1DDZD11D224400;40440D111Z1DDDZ\nZZZD11Z1ZD1Z11D111111004242040240D1D11ZDDZ1Z\nDZZ11ZZD11D1Z1D1D1DD0022F400420ZDZZDZD1Z1Z11\nZD1DD0201Z1ZDDDD11ZDD42C0F02244ZDDZZZZZ11DZZ\nDD1Z02FCF01ZZZZ1DZD1D400C22440D1D1DDZ1DDDZDZ\nZC40442421DD1Z1ZD1D12242021Z1ZD11ZZZ1ZZ1DZ1Z\n33F042F242Z11Z111ZDZZ1D111ZDDZ1ZD1DZ1D11D111\nD3000440204441ZZ11Z111Z1ZD11DD1DDZDDD1D1ZZZD\nZ11DD1DD1D0C4ZZZ1ZDZDD11D1ZDZDDZZD1Z1ZDZ1DD1\nZDZZZ11ZD110ZZ1DZZ1ZZD20204ZZZZDDDZD1Z1DZ11D\n1Z1ZDZDDZZDZ1Z1ZZ11D12040C2411DDZ1Z1DDZZ1ZZZ\nZ1Z1DZ11DD111ZZDDZZ11D1230320D1D1ZDDZDDZ1ZDD\n1DZ1ZZDDDDD1D1D1D111DDD2232011ZDZ1Z1DD11ZZZD\nD1DZZ1ZDDD11ZZDZDD1ZZD02211ZDDDDDZZZZDDZD1ZZ\nDZDD1ZDDZDZZZDDD111DZZDZ1Z1Z11DD1Z1DDZ1DZDDZ\n111ZDZDZDZDZZD1ZZ1ZZZD11Z1DDDDDZZDZ1DZZ11ZD1\nZDDDZZ1Z1ZZ1DD11ZZ1DDDZZZ1DZD1DD11DZZZ11DD1D\n19*1A37R##*||*||#|#*#||||*|##|*||*|*||*|*##*\nF)|CR87|*#|#||**#|##||*##|||#||#|##*#*#||*|#\n29|GRASS#*#*||#**|#||**##|#|***||||*||**#*##\n;9|!OUNFAIN|#*#*|#*|#**#|*||||*|***#****#|*#')

ddict = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.',
'2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E',
'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ',
'#': ' '}
print(find_treasure('decoded_map2.txt'))
