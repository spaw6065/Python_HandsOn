import datetime
import logging
import sys

logger = logging.getLogger()

#Create and configure logger
fileName=format(datetime.datetime.now(),"%Y%m%d")

logging.basicConfig(filename="C:/Users/SumitPawar/Python_classes/"+fileName,
                    format='%(asctime)s %(message)s',
                    filemode='w')

# print to console
logger.setLevel("INFO")

scriptName = sys.argv[0]
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

logger.info("sum of %d and %d is %d",num1,num2,num1+num2)
