import json

from src.models.operation import Operation


def load_operation(path: str) -> list[dict]:
    with open(path) as file:
        return json.load(file)


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    list_ = []
    for operation in operations:
        if operation:
           list_.append(
               Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                _from=operation.get("from", ""),
                _to=operation["to"],
            )
        )
    return list_


def get_executed_operation_instances(operations: list[Operation]) -> list[Operation]:
    operation_list = []
    for operation in operations:
        if operation.state == "EXECUTED":
            operation_list.append(operation)
     return operation_list


from datetime import datetime

def sort_operation_instances(operations: list[Operation]) -> list[Operation]:
    # Сортируем операции по дате в убывающем порядке (от последней к первой)
    sorted_operations = sorted(operations, key=lambda op: datetime.fromisoformat(op.date), reverse=True)
    return sorted_operations


