# encoding: utf-8
from nlp.embedding.api import BertEmbedding
import time
import torch
import os
import sqlite3
import pandas as pd
from tqdm import tqdm
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = BertEmbedding()
feature_path = os.path.join(BASE_DIR, 'data/job_feature.pt')
sqlite_path = os.path.join(BASE_DIR, 'db.sqlite3')
data_desc_path = os.path.join(BASE_DIR, 'data/data_desc.csv')
id_sql = "select id FROM job WHERE jid='{}' and lid='{}'"

while True:
    try:
        print("---------------- Start ----------------")
        job_feature = {}
        if os.path.exists(feature_path):
            job_feature = torch.load(feature_path)
        conn = sqlite3.connect(sqlite_path)
        cursor = conn.cursor()
        data_desc = pd.read_csv(data_desc_path, header=None)
        print("total len", len(data_desc))
        for index, row in tqdm(data_desc.iterrows()):
            try:
                sql = id_sql.format(row[0], row[1])
                cursor.execute(sql)
                jobId = next(cursor)[0]
                if jobId in job_feature.keys():
                    continue
                job_feature[jobId] = model.bert_embedding(row[2])
            except Exception as e:
                continue
        conn.close()
        torch.save(job_feature, feature_path)
        print("---------------- Finish ----------------")
        time.sleep(60*60*24)
    except Exception as e:
        conn.close()
        print(str(e))
        time.sleep(60*60*24)
