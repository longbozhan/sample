#coding:utf8

import logging
import logging.handlers
from logutils.queue import QueueHandler, queue
import os
import time
from logging.handlers import TimedRotatingFileHandler

"""
只是重写了TimedRotatingFileHandler的doRollover部分，参考：https://www.jianshu.com/p/d615bf01e37b
在windows下的os.rename还是会出现 “另一个程序正在使用此文件，进程无法访问”
"""

class SafeRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):
        TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc)

    """
    Override doRollover
    lines commanded by "##" is changed by cc
    """

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.

        Override,   1. if dfn not exist then do rename
                    2. _open with "a" model
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        ##        if os.path.exists(dfn):
        ##            os.remove(dfn)

        # Issue 18940: A file may not have been created if delay is True.
        ##        if os.path.exists(self.baseFilename):
        if not os.path.exists(dfn) and os.path.exists(self.baseFilename):
            os.rename(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.mode = "a"
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


def get_logger(name='root', sync_terminal=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 添加TimedRotatingFileHandler
    timefilehandler = SafeRotatingFileHandler(
        "log",    #日志路径
        when='MIDNIGHT',      # S秒 M分 H时 D天 W周 按时间切割 测试选用S
        interval=1,    # 多少天切割一次
        backupCount=30  # 保留多少天
    )
    # 设置后缀名称，跟strftime的格式一样
    #timefilehandler.suffix = "%Y%m%d.log"
    formatter = logging.Formatter('%(asctime)s - %(process)d - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    timefilehandler.setFormatter(formatter)

    q = queue.Queue(-1)
    queue_handler = QueueHandler(q)
    logger.addHandler(queue_handler)
    logger.addHandler(timefilehandler)

    if sync_terminal:
        streamHandler = logging.StreamHandler()#往屏幕上输出
        streamHandler.setFormatter(formatter) #设置屏幕上显示的格式
        logger.addHandler(streamHandler)
    return logger

log = get_logger("sqlalchemy", sync_terminal=True)


def test_log_fun():
    log.info("in child, before sleep")
    import time
    count = 5
    while count > 0:
        log.info("in child, count:%s" % (count))
        count -= 1
        time.sleep(1)
    log.info("in child, sleep done, exit")

if __name__ == "__main__":
    from multiprocessing import Process
    log.info("in main, before process")
    log_list = []
    for i in range(10):
        p = Process(target=test_log_fun)
        p.start()
        log_list.append(p)
    for lst in log_list:
        lst.join()
    log.info("in main, exit")
