# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    input_fp = open('2015taiwan.txt', 'r')
    output_fp = open('output.txt', 'w')
    for line in input_fp:
        line_list = line.split(',')
        if line_list[2] != "PM2.5":
            continue
        else:
			location = line_list[1].decode('big5').encode('utf-8')
            output_fp.write(str(line_list).decode('big5'))
            output_fp.write('\n')
            print location
