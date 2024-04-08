from flask import Request, current_app
from ..models.user import User

from ..helpers.api_responser import ApiResponser
from ..helpers.validate_user import ValidateUser


class UserController:
    @staticmethod
    def loanProcess(request: Request):
        user_data = ValidateUser.validateData(request.json)
        user = User(**user_data)
        request_amount = user.request_amount
        reference_value = current_app.config.get("REFERENCE_VALUE")
        status = "Approved"

        if request_amount > reference_value:
            status = "Declined"
        elif request_amount == reference_value:
            status = "Undecided"

        return ApiResponser.successReponse(status)
