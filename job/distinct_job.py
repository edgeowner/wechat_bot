# from wxpy import *
# from apscheduler.schedulers.blocking import BlockingScheduler
# from config.config import cfg
# from msg_drop_duplicates import Dropduplicates
#
# sched = BlockingScheduler()
#
# # robot = Bot(cache_path=True, console_qr=cfg.getint('CONSOLE_QR'), logout_callback=sys.exit)
#
# # robot.groups(update=True, contact_only=False)
# # groups = robot.groups()
# #
# # itchat = robot.core
#
#
# @sched.scheduled_job('interval', hours=24, start_date='2018-12-25 17:55:00')
# def job_function():
#     print("***************************** START Job_function ******************************")
#     dropduplicates = Dropduplicates()
#     dropduplicates.drop_dulicates()
#     print("***************************** END Job_function ******************************")
#
#
# if __name__ == '__main__':
#     log = logging.getLogger('apscheduler.executors.default')
#
#     log.setLevel(logging.INFO)  # DEBUG
#     #
#     fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
#     h = logging.StreamHandler()
#     h.setFormatter(fmt)
#     log.addHandler(h)
#     print('drop  duplicates start to do it')
#     # Schedules job_function to be run on the third Friday
#     #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
#     # sched.add_job(job_function, 'cron', day_of_week='0-6', hour='0-9', minute="*", second="*/4")
#     # sched.add_job(job_function())
#     # sched.add_job(job_function,'interval',)
#     # str = '@bcc303451a0b4abefa574b055c9a383acba026a68139affc2d59bdf49cb53863'.encode()
#     # count = int(hashlib.sha1(str).hexdigest(), 16) % (10 ** 18)
#     # print(count)
#     # hash_object = hash()
#     # print(hash_object.hexdigest())
#     sched.start()
