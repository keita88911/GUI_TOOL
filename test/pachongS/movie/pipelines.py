class MoviePipeline(object):
    def process_item(self, item, spider):
        with open("my_meiju.txt",'a') as fp:
            fp.write(item['name'].encode("utf8") + '\n')