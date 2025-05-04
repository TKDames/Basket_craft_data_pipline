SUMMARY

This repository showcases a complete data pipeline built for Basket Craft to move and transform web session data from source to dashboard. 
Using Python and SQLAlchemy, the pipeline first extracts December 2023 session data from a MySQL database hosted on AWS RDS, 
then loads it into a raw schema within a Postgres warehouse, also on RDS. From there, dbt models reshape the raw data into clean, structured layers for analysis. 
The project is developed within GitHub Codespaces, with GitHub Actions and Secrets managing automated runs and secure credentials. Finally, the data feeds into Looker Studio, 
where it's visualized in an interactive dashboard. Every component—from the initial data extraction to the final dashboard—is version-controlled with Git and designed to scale with future datasets and insights.

LINK TO Looker
https://lookerstudio.google.com/s/rBzKkGH3niE 

