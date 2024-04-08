from flask import Blueprint
from ..exceptions import UserNotValid
from ..helpers.api_responser import ApiResponser

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(UserNotValid)
def handle_user_exceptions(error: Exception):
    return ApiResponser.errorResponse(error)
