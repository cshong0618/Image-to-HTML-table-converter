from PIL import Image
import numpy as np
import sys

def nparr_to_tuple(nparr):
    l = []
    for i in nparr:
        l.append(i)

    return tuple(l)

def tuple_to_hex(tup):
    s = '#%02x%02x%02x' % tup
    return s

def generate_table(imarr):
    header = '<style>td{width:1px;height:1px}</style><table border="0" cellpadding="0" cellspacing="0"><tbody>'

    body = header
    for row in range(0, imarr.shape[0], 2):
        body += '<tr>'
        for col in range(0, imarr.shape[1], 2):
            if np.all(imarr[row, col] == 255):
                body += '<td></td>'
            else:
                body += '<td bgcolor="' + tuple_to_hex(nparr_to_tuple(imarr[row, col])) + '"></td>'
        body += '</tr>'

    body += '</tbody></table>'

    return body

def read_image(path):
    im = Image.open(path)
    imarray = np.array(im)
    im.close()
    return imarray

def main():
    print(sys.argv)
    output = ''
    if len(sys.argv) == 1:
        msg = 'Image to HTML Tables script\n' \
              '[program-name] [arg1] [arg2]=optional\n' \
              'arg1 = Input filename\n' \
              'arg2 = Output filename\n' \
              '*If output filename is not given, output filename will be input filename with html extension*\n'
        print(msg)
        return 1
    else:
        output = generate_table(read_image(sys.argv[1]))

    if len(sys.argv) == 2:
        fo = open(sys.argv[1] + '.html', 'w')
        fo.write(output)
        fo.close()
    elif len(sys.argv) == 3:
        fo = open(sys.argv[2], 'w')
        fo.write(output)
        fo.close()
    else:
        print("Wrong number of arguments")


if __name__ == "__main__":
    main()