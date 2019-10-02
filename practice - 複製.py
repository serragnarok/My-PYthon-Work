stop = '想結束請...打\'謝謝財哥....\''
message = ''
mes = []

print(stop)
while message != '謝謝財哥...':
    message = input('財哥...專業...檳榔攤...：')
    for i in range(len(message)):
        if i % 2 == 0:
            mes.append(message[i:i+2])
    mes.append('   ')
    m = '...'.join(mes)
    print(m)
    
    mes = []
else:
    print('看來...檳主...盡歡...')



