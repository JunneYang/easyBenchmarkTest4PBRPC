#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs

def dataformater(src_file,dst_file):
    try:
        fr=codecs.open(src_file,'r','gbk')
        ls=fr.readlines()
        fr.close()

        fw=codecs.open(dst_file,'w','gbk')
        for line in ls:
            fw.write("bnitems\t"+line)
        fw.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    dataformater("nuomi_recomend_list_20140623_test_gbk_formal.txt","dataformater_bnitems.data")