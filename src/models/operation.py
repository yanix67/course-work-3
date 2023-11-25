from datetime import datetime

def convert_payment(payment: str) -> str:
    if payment.startswith("Счет"):
        return '**' + payment[-4:]
    else:
        if payment.replace(" ", "").isdigit() and len(payment.replace(" ", "")) >= 16:
            card_digits = payment.replace(" ", "")
            masked = card_digits[:6] + ' XX** **** ' + card_digits[-4:]
            return masked
        else:
            return "**XX"


class Operation:
    def __init__(
        self,
        pk: int,
        state: str,
        date: str,
        operation_amount: dict,
        description: str,
        _from: str,
        _to: str
    ):
        self.pk = pk
        self.state = state
        self.date = self.convert_date(date)
        self.operation_amount = operation_amount
        self.description = description
        self._from = _from
        self._to = _to

    def convert_date(self, date: str) -> datetime:
        return datetime.fromisoformat(date)

    def __str__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.convert_payment(self._from)} -> {self.convert_payment(self._to)}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n")
