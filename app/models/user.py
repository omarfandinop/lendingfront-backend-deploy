from ..exceptions import UserNotValid


class User:
    def __init__(
        self, tax_id: str, business_name: str, request_amount: int, **kwargs
    ) -> None:
        self.tax_id = tax_id
        self.business_name = business_name
        self.request_amount = request_amount

        if kwargs:
            unexpected_fields = list(kwargs.keys())
            raise UserNotValid(f"Unexpected parameters: {unexpected_fields}")
