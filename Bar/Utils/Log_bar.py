import logging as log
import os

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler(os.getcwd() + '/logs/bar.log'),
                    log.StreamHandler()
                ])
