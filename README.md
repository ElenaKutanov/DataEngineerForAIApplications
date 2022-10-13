# Data Engineer for AI applications
## Bosch AI Talent Accelerator

### Project: TechTrends
(Docker, DockerHub, GitHub Actions, Kubernetes, Vagrant, Helm, ArgoCD, CI/CD, Python)

Packaged the application by creating a Dockerfile and Docker image.
Implemented Continuous Integration (CI) practices by using GitHub Actions to automate the build and push of the Docker image to DockerHub.
Constructed the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster was provisioned using k3s in a vagrant box.
Created templates for the Kubernetes manifests using a Helm chart and provided the input configuration files for staging and production environments.
Implemented the Continuous Delivery (CD) practices by deploying the application to staging and production environments using ArgoCD and the Helm chart.

### Project: Data Pipelines
(AWS, Airflow, Python)

Created and automated a set of data pipelines with Airflow, monitoring and debugging production pipelines

### Project: Data Lake
(Spark on Hadoop, AWS, S3, Jupyter Notebook, EMR, ETL, Python)

Built a data lake and an ETL pipeline in Spark that loads data from S3, processes it into analytics tables, and loads them back into S3

### Project: Data Warehouse
(AWS, Redshift, S3, ETL, SQL, Python)

Built an ETL pipeline that extracts data from S3 and stages them in Redshift, and transforms data into a set of dimensional tables

### Project: Data Modeling with Apache Cassandra
(Cassandra, Python)

### Project: Data Modeling with Postgres
(Postgres, ETL, SQL, Python)