import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, documents: func.DocumentList, outdocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("{}".format(documents[0]))
    logging.info("{}".format(documents[0]["count"]))

    count = documents[0]["count"]
    updated_count = count + 1
    count_json = json.dumps({"count": count})

    updated_count_json = json.dumps({"id": "1", "count": updated_count})

    outdocument.set(func.Document.from_json(updated_count_json))


    return func.HttpResponse("{}".format(count_json))

