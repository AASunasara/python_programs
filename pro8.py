'''
8: Program to Generate random logs and write in a file , once the file size reaches 2Mb
open new file and continue writing
'''
import logging, time
import logging.handlers as handlers


def main():
    logger = logging.getLogger('test_pro8')
    log_hnd = handlers.RotatingFileHandler('files/pro8_logs/pro8.log', maxBytes=2000000, backupCount=5)
    log_hnd.setLevel(logging.INFO)
    logger.addHandler(log_hnd)
    
    print("Started geerating logs....")
    while True:
        time.sleep(0.1)
        logger.info("logging test for program 8 at xyz")

if __name__ == "__main__":
    main()