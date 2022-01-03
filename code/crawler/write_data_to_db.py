import sqlite3
import pandas as pd
import os
os.chdir(os.path.dirname(__file__))


def format_insert_str(template: str, values: list):
    values = [f'"{v}"' if isinstance(v, str) else v for v in values]
    return template.format(*values)


conn = sqlite3.connect('../backend/db.sqlite3')
cursor = conn.cursor()


# bigjob_data = pd.read_csv('./104Jobs.csv')
# bigjob_data = bigjob_data.fillna('')
# bigjob_sql_template = "insert into bigJob (jobName, jobCat, jobDesc ,bigJobImg, holland1,holland2,holland3,jobWork,subject1,subject2) values ({},{},{},{},{},{},{},{},{},{})"
# for i, row in bigjob_data.iterrows():
#     try:
#         values = [row.jobName, row.jobCat, row.jobDesc,
#                   row.bigJobImg, row.holland1, row.holland2, row.holland3,
#                   row.jobWorks, row.subject1, row.subject2]
#         sql = format_insert_str(bigjob_sql_template, values)
#         cursor.execute(sql)
#         conn.commit()
#     except Exception as e:
#         print(e)
#         conn.rollback()


header = ['jobName', 'jobSubName', 'jid',
          'lid', 'jobSalary', 'jobLimitExperience',
          'jobLimitStudy', 'jobArea', 'companyName',
          'jobIndustry', 'financialStatus', 'scale',
          'companyLogo', 'bonus']
job_data = pd.read_csv('./data.csv', header=None)
job_data.columns = header
job_data = job_data.fillna('')
job_sql_template = "insert into job (jobName, jobSalary, jobLimitExperience, jobLimitStudy, jobArea, companyName, financialStatus, scale, companyLogo, bonus, jobIndustry, jobSubName, jid, lid) values ({},{},{},{},{},{},{},{},{},{},{},{},{},{})"
for i, row in job_data.iterrows():
    try:
        values = [row.jobName, row.jobSalary, row.jobLimitExperience,
                  row.jobLimitStudy, row.jobArea, row.companyName, row.financialStatus,
                  row.scale, row.companyLogo, row.bonus, row.jobIndustry, row.jobSubName, row.jid, row.lid]
        sql = format_insert_str(job_sql_template, values)
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


# related_job = pd.read_csv('./relatedjob.csv')


conn.close()
