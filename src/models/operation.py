from datetime import datetime


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
        self._from = self.convert_payment(_from)
        self._to = self.convert_payment(_to)


    def convert_date(self, date: str, iso_date=None) -> str:
        date = datetime.fromtimestamp(iso_date)
        return date.strftime("%d/%m/%Y")

    def convert_payment(self, _from):
        pass


def convert_payment(self, payment: str):
    if payment:
        if payment.startswith("Счет"):
            return payment  # Номер счета не требует маскировки
    else:
        # Проверяем, является ли входная строка номером карты
        if payment.isdigit() and len(payment) >= 16:
            # Форматируем номер карты в заданный формат
            masked = payment[:6] + ' XX** **** ' + payment[-4:]
            return masked
        else:
            return "**XX"  # Возвращаем маску, если номер карты не распознан


  def __str__(self):
      return (f"{self.date} {self.des}\n"
              f"{self._from} -> {self._to}\n"
              f"{self.operation_amount['amount']} {self.operation_amount['name']}\n")