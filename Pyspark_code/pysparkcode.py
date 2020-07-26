from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").master("local[*]").getOrCreate()

df = spark.read.format("csv").option("header",True).option("inferSchema",True).load("C:/Users/SumitPawar/Python_classes/Pyspark/emp.csv")
df.show(20)

df.select("empid","empname","esalary").sort(df.esalary.desc()).show()