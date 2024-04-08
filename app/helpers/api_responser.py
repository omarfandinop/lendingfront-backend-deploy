from flask import jsonify


class ApiResponser:
    @staticmethod
    def successReponse(data, code=200):
        response = jsonify(data)
        response.status_code = code
        return response

    @staticmethod
    def errorResponse(error, code=400):
        message = {"error": str(error), "errorType": type(error).__name__}
        response = jsonify(message)
        response.status_code = code
        return response
