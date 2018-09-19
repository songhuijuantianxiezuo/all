import logging
def log()
    f = '%(asctime)-10s  %(username)-5s  %(password)-10s  %(message)-5s'
    logging.basicConfig(format = f)
    d = {'username':'testuser1','password':'123456'}
    logging.warning('problem:%s','no',extra=d)