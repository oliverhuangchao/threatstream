import sys
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":

    # def merge_lines(x,y):
    #     return x+y
    def replace_word(text):
        if text[:2] == '<%' and text[-2:] == '%>' and text[2:-2] in check:
            text = check[text[2:-2]]


        # size = len(text)
        # start = -1
        # end = -1
        # for i in range(size-1):
        #     if text[i:i+2] == '<%':
        #         start = i+2
        #     if text[i:i+2] == '%>':
        #         end = i
        #     if start >= 0 and end >= 0 and text[start:end] in check:
        #         #print ori[start:end]
        #         text = text[:start-2] + check[text[start:end]] + text[end+2:]
        #         start = -1
        #         end = -1
        # return text

    # ------run on the master node------
    if len(sys.argv) != 2:
        #print("you should add a text file in the end", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="threatstream2")
    lines = sc.textFile(sys.argv[1], 1) #or user hadoopFile instead
    check = {'aaa':'dream','bbb':'the'}
    #check.persist() # in that case, this hashtable will be saved on the memory in each node

    # ------run on the master node------
    words = lines.flatMap(lambda line: lines.split(' ')).map(replace_word)
    print(words)
    z = " ".join(word_list)
    pairs = z.map(lambda x:(x,1))
    output = pairs.collect()
    print(output)


    #counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    #output = counts.collect()
    #for (word, count) in output:
    #    print("%s: %i" % (word, count))

    sc.stop()