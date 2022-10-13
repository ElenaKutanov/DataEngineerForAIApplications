# Sparkify Data Lake

Because of the growing user base and songs database there was the decision about moving the data warehouse to a data lake.

The Sparkify data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. In the project was created a ETL pipeline that extracts the data from S3, processed using Spark, and loaded the data back into S3 as a set of dimensional tables. The deployment with Spark process is on a cluster using AWS.

The tables will allow the analytics team to continue finding insights in what songs their users are listening to.