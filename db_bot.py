import json
from openai import OpenAI
import os
import sqlite3
from time import time

print("Running db_bot.py!")

fdir = os.path.dirname(__file__)
def getPath(fname):
    return os.path.join(fdir, fname)

# SQLite
sqliteDbPath = getPath("aidb.sqlite")
setupSqlPath = getPath("db_structure.sql")
setupSqlDataPath = getPath("db_data.sql")

# erase previous db
if os.path.exists(sqliteDbPath):
    os.remove(sqliteDbPath) 

sqliteCon = sqlite3.connect(sqliteDbPath) # create new db
sqliteCursor = sqliteCon.cursor()
with (
        open(setupSqlPath) as setupSqlFile,
        open(setupSqlDataPath) as setupSqlDataFile
    ):

    setupSqlScript = setupSqlFile.read()
    setupSQlDataScript = setupSqlDataFile.read()

sqliteCursor.executescript(setupSqlScript) # setup tables and keys
sqliteCursor.executescript(setupSQlDataScript) # setup tables and keys

def runSql(query):
    result = sqliteCursor.execute(query).fetchall()
    return result

# OPENAI
configPath = getPath("config.json")
print(configPath)
with open(configPath) as configFile:
    config = json.load(configFile)

openAiClient = OpenAI(api_key = config["openaiKey"])

def getChatGptResponse(content):
    stream = openAiClient.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    responseList = []
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            responseList.append(chunk.choices[0].delta.content)

    result = "".join(responseList)
    return result


# strategies
commonSqlOnlyRequest = "Provide an SQLite SELECT statement that answers the following question. Respond only with SQLite syntax. Do not include any explanations, even for errors."
strategies = {
    "zero_shot": setupSqlScript + commonSqlOnlyRequest,
    "single_domain_double_shot": (setupSqlScript + 
                   "What are the names of all students majoring in Computer Science?" + 
                   "\nSELECT name\nFROM student\nWHERE major = 'Computer Science';\n" +
                   commonSqlOnlyRequest)
}

questions = [
    "Which courses are taught by Dr. John Miller?",
    "Which students are enrolled in the 'Introduction to Programming' course?",
    "Which professors teach more than one course?",
    "List all students along with the courses they are enrolled in.",
    "Which students have taken at least two courses and received all A's?",
    "Which classroom is used the most based on scheduled courses?"
]

def sanitizeForJustSql(value):
    gptStartSqlMarker = "```sql"
    gptEndSqlMarker = "```"
    if gptStartSqlMarker in value:
        value = value.split(gptStartSqlMarker)[1]
    if gptEndSqlMarker in value:
        value = value.split(gptEndSqlMarker)[0]

    return value

for strategy in strategies:
    responses = {"strategy": strategy, "prompt_prefix": strategies[strategy]}
    questionResults = []
    for question in questions:
        print(question)
        error = "None"
        try:
            sqlSyntaxResponse = getChatGptResponse(strategies[strategy] + " " + question)
            sqlSyntaxResponse = sanitizeForJustSql(sqlSyntaxResponse)
            print(sqlSyntaxResponse)
            queryRawResponse = str(runSql(sqlSyntaxResponse))
            print(queryRawResponse)
            friendlyResultsPrompt = "I asked this question \"" + question +"\" and the response was \""+queryRawResponse+"\" Please, simply provide a concise response in a more user-friendly way. Please do not include any other suggestions/chatter."
            friendlyResponse = getChatGptResponse(friendlyResultsPrompt)
            print(friendlyResponse)
        except Exception as err:
            error = str(err)
            print(err)

        questionResults.append({
            "question": question, 
            "sql": sqlSyntaxResponse, 
            "queryRawResponse": queryRawResponse,
            "friendlyResponse": friendlyResponse,
            "error": error
        })

    responses["questionResults"] = questionResults

    with open(getPath(f"response_{strategy}.json"), "w") as outFile:
        json.dump(responses, outFile, indent = 2)
            

sqliteCursor.close()
sqliteCon.close()
print("Done!")
