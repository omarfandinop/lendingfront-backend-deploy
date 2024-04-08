from flask import Blueprint, request
from ..controllers.user_controller import UserController
from ..helpers.api_responser import ApiResponser

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def welcome():
    return ApiResponser.successReponse({"welcome": "Welcome to Loan API"})


@api.route("/loan", methods=["POST"])
def loan():
    return UserController.loanProcess(request)
