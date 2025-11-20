import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="Predict")
def Predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure')
    monthly = req.params.get('monthly')
    techsupport = req.params.get('techsupport')

    predicition = make_prediction(
        tenure = tenure,
        MonthlyCharges = monthly,
        TechSupport_yes = techsupport
    )


    if tenure and monthly and techsupport :
        return func.HttpResponse(f"Hello. The probability that this customer will churn is {predicition}")
    else:
        return func.HttpResponse(
             "Function triggered succesfully. Pass tenure, monthly, techsupport to get a predicition.",
             status_code=200
        )