import codecs
if __name__ == '__main__':
    input_fp = codecs.open('2015taiwan.txt','r',encoding = 'utf8')
    output_fp = codecs.open('output.txt','w')
    for line in input_fp:
        line_list = line.split(',')
        if line_list[2] != "PM2.5":
            continue
        else:
            output_fp.write(str(line_list))
            output_fp.write('\n')
