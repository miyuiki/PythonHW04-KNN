# coding = utf8
import codecs
import sys
if __name__ == '__main__':
    input_fp = codecs.open('2015taiwan.txt', 'r')
    output_fp = codecs.open('output.txt', 'w')
    for line in input_fp:
        line_list = line.split(',')
        if line_list[2] != "PM2.5":
            continue
        else:
            line_list[1] = line_list[1].encode('big5')
            output_fp.write(str(line_list).decode('big5'))
            output_fp.write('\n')
            print line_list
