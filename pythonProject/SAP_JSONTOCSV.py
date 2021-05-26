import pandas as pd
from pandas import json_normalize
import json

with open(r'C:\Users\Shashi Kumar\SAP\input.json') as f:
    resultData = json.load(f)
    # print(resultData)
    bodyData = resultData[0]["Body"]
    bodyProblemsData = bodyData["problems"]
    # print(bodyProblemsData)
    csvOutputList = []
    FILTER_CONST = "SERVICES"
    for i in bodyProblemsData:
        if i["impactLevel"] == FILTER_CONST:
            tempObj = {
                       "id": i["impactedEntities"][0]["entityId"]["id"],
                       "name": i["impactedEntities"][0]["name"],
                       "impactLevel": i["impactLevel"],
                       "title": i["title"],
                       "severityLevel": i["severityLevel"]
                       }
            csvOutputList.append(tempObj)

    print(csvOutputList)
    jsonSerializeData = json_normalize(csvOutputList)
    print(jsonSerializeData)
    jsonSerializeData.to_csv(r'C:\Users\Shashi Kumar\SAP\sap_interview_output.csv', index= False)
