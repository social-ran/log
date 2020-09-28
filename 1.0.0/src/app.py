import asyncio
import os
import datetime,time
from walkoff_app_sdk.app_base import AppBase

class logger(AppBase):
    __version__ = "1.0.0"
    app_name = "log"  # this needs to match "name" in api.yaml
    def __init__(self, redis, logger, console_logger=None):
        super().__init__(redis, logger, console_logger)

    async def log(self,appname):
        os.system('sshpass -p '+'123456'+ ' scp 10.245.142.21:root/shuffle_log.txt '+'/home')
        fp = open('/home/shuffle_log.txt', 'w')
        nowtime = datetime.datetime.now()
        str_time = nowtime.strftime("%Y-%m-%d %X")
        fp.write(appname+' finished in: '+str_time )
        fp.close()
        os.system('sshpass -p '+'123456'+ ' scp /home/shuffle_log.txt '+'10.245.142.21:/root')
        os.system('rm -r /home/shuffle_log.txt')
        return "OK!!"

    async def readlog(self):
        os.system('sshpass -p '+'123456'+ ' scp 10.245.142.21:root/shuffle_log.txt '+'/home')
        fp = open('/home/shuffle_log.txt', 'r')
        str=fp.read()
        return str


    async def clearlog(self):
        os.system('touch shuffle_log.txt')
        os.system('sshpass -p ' + '123456' + ' scp /home/shuffle_log.txt ' + '10.245.142.21:/root')
        os.system('rm -r shuffle_log.txt')
        return "OK!!"



if __name__ == "__main__":
    asyncio.run(logger.run(), debug=True)
