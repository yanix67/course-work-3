import os

from src.models.operation import Operation
from src.utils import load_operation, get_operation_instances


def test_load_operation(pytest=None):
    path = os.path.join(os.path.dirname(__file__), "data", "")
    operation = load_operation(path)
    assert len(operation) == 5
    assert operation[0]["id"] == 441945886

    path = os.path.join(os.path.dirname(__file__), "data", "operations.json")
    with pytest.raises(FileNotFoundError):
        load_operation(path)


def test_get_operation_instances(pytest=None):
    test_operation = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {}
    ]
    operations_instances = get_operation_instances(test_operation)
    assert isinstance(operations_instances, list)
    assert isinstance(operations_instances[0], Operation)
    assert operations_instances[0].pk == 441945886
    assert operations_instances[0].state == "EXECUTED"
    assert operations_instances[0].date == "2019-08-26T10:50:58.294041"
    assert operations_instances[0].operation_amount.amount == "31957.58"
    assert operations_instances[0].operation_amount.currency.name == "руб."
    assert operations_instances[0].operation_amount.currency.code == "RUB"
    assert operations_instances[0].description == "Перевод организации"
    assert operations_instances[0]._from == "Maestro 1596837868705199"
    assert operations_instances[0]._to == "Счет 64686473678894779589"
    assert operations_instances[1] == {}

    test_operations = []
    operations_instances = get_operation_instances(test_operations)
    assert operations_instances == []

    test_operations = [{}]
    operations_instances = get_operation_instances(test_operations)
    assert operations_instances == []

    test_operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 64686473678894779589"
        },
    ]
    operations_instances = get_operation_instances(test_operations)
    assert isinstance(operations_instances, list)
    assert isinstance(operations_instances[0], Operation)
    assert operations_instances[0]._from == ""
