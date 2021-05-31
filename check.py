import csv
import numpy as np

with open('qet_sart_checked.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ppts = {}
    for row in reader:
        ppt = row['observation']
        if not ppt in ppts:
            ppts[ppt] = []

        resp = row['response_timestamp']
        if resp and not resp == "NA":
            ppts[ppt].append(float(resp) - float(row['time_render']))

    for x in ppts.keys():
        data = np.array(ppts[x])
        print(f"obs {x}, mean: {data.mean():.2f} sd: {data.std():.2f}")


    from IPython import embed; embed() 
