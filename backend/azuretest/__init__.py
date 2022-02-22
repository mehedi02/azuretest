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


    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
