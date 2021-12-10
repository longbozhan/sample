# -*- coding: utf-8 -*-

import os
import threading
from configparser import ConfigParser, NoOptionError
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

lock = threading.Lock()

"""
基于ConfigParser的日志库，支持热加载，程序不需要重启，支持传入自定义配置路径，默认从./conf/app.conf加载
"""

class ConfigFileModifyHandler(FileSystemEventHandler):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
    def on_modified(self, event):
        #print "event.src_path:%s config_file_path:%s" % (event.src_path, self.config_file_path)
        if os.path.relpath(event.src_path) == os.path.relpath(self.config_file_path):
            Config.get_instance().load_config()


class Config(object):
    __instance = None

    def __init__(self, config_file_path=None):
        self.config = ConfigParser()
        self.config_file_path = config_file_path or os.path.join(os.getcwd(), './conf/app.conf')
        self.load_config()
        self._init_config_file_observer()

    def _init_config_file_observer(self):
        event_handler = ConfigFileModifyHandler(self.config_file_path)
        observer = Observer()
        observer.schedule(event_handler, path=os.path.dirname(self.config_file_path), recursive=False)
        observer.setDaemon(True)
        observer.start()

    @staticmethod
    def get_instance():
        if Config.__instance:
            return Config.__instance
        try:
            lock.acquire()
            if not Config.__instance:
                Config.__instance = Config()
        finally:
            lock.release()
        return Config.__instance

    def load_config(self):
        self.config.read(self.config_file_path, 'utf-8')

    def get(self, section, option, default=None):
        if not self.config.has_section(section):
            return default
        try:
            return self.config.get(section, option)
        except NoOptionError:
            return default
    def getint(self, section, option, default=None):
        if not self.config.has_section(section):
            return default
        try:
            return self.config.getint(section, option)
        except NoOptionError:
            return default
    def getfloat(self, section, option, default=None):
        if not self.config.has_section(section):
            return default
        try:
            return self.config.getfloat(section, option)
        except NoOptionError:
            return default

g_conf = Config.get_instance()


if __name__ == "__main__":
    import time
    while True:
        print("value:%s" % (g_conf.get("section_test", "option_test")))
        print("value2:%s" % (g_conf.getint("section_test", "option_test2", 2)))
        print("value3:%s" % (g_conf.getfloat("section_test", "option_test3", 3.0)))
        time.sleep(1)
