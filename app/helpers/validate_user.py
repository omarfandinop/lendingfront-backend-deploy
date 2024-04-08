from ..exceptions import UserNotValid


class ValidateUser:
    @staticmethod
    def validateData(data):
        if not data:
            raise UserNotValid("The request must be of type JSON")

        required_fields = ["tax_id", "business_name", "request_amount"]
        missing_fields = [
            field
            for field in required_fields
            if isinstance(data.get(field), bool)
            or not isinstance(data.get(field), (str, int))
            or (isinstance(data.get(field), str) and data.get(field).strip() == "")
        ]

        if missing_fields:
            raise UserNotValid(
                f'The following fields are required: {", ".join(missing_fields)}'
            )

        amount_key = "request_amount"
        request_amount = data.get(amount_key)

        if isinstance(request_amount, int) or (
            isinstance(request_amount, str) and request_amount.isdigit()
        ):
            data[amount_key] = int(request_amount)
        else:
            raise UserNotValid(f"'{amount_key}' is not valid")

        return data
