import logging

def f_w():
    # create logger with 'spam_application'
    logger = logging.getLogger('CNode_eeddclub')   #标题
    logger.setLevel(logging.NOTSET)  #起始打印的水平
    # create file handler which logs even debug messages
    fh = logging.FileHandler('spam.log')    #日志锁所在的文件
    # fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  #日志的格式
    fh.setFormatter(formatter)    #将fh套入该格式中
    # ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)    #将fh添加到日志中
    # logger.addHandler(ch)
    return logger  #返回日志
l=f_w()
l.info("lll2")
l.debug('dsdssf')
l.warning('sdfdfsdd')
l.error('dssdfsf')   #虽然没有提示，但是warning和error是可以打印出来的，但是error需要小写来调，大写无法打印
