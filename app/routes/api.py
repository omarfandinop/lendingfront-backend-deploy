from flask import Blueprint, request, current_app
from ..controllers.user_controller import UserController
from ..helpers.api_responser import ApiResponser

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def welcome():
    reference_value = current_app.config.get("REFERENCE_VALUE")
    return ApiResponser.successReponse(
        {"welcome": f"Welcome to Loan API {reference_value}"}
    )


@api.route("/loan", methods=["POST"])
def loan():
    return UserController.loanProcess(request)
