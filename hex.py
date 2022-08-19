import idc

def fun():
    begin = 0x403040; #需对应修改
    size = 114        #需对应修改
    #list = []
    for i in range(size):
        byte_tmp = idc.get_wide_byte(begin + i*4)
        #list.append(byte_tmp)
        print(byte_tmp,end=",")
    print('collect over')

    
fun()