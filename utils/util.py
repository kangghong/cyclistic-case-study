def nullProportions (data):

    null_percents = {}

    for col in data.columns:

        null_percents[col] = (int(data[col].isnull().sum())/ int(data.shape[0]))*100

    return null_percents

def verifyConcat (past_year_data, merged_data):
    totalRows = 0

    for data in past_year_data:

        totalRows += data.shape[0]

    return totalRows == merged_data.shape[0]