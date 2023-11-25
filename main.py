from src.models.operation import convert_payment
from src.utils import load_operation, get_operation_instances, sort_operation_instances
from datetime import datetime


def get_executed_operations(operations):
    return filter(lambda op: op.state == 'EXECUTED', operations)


def main():
    operations = load_operation("src/data/operations.json")
    operations_instances = get_operation_instances(operations)
    executed_operations = get_executed_operations(operations_instances)
    sorted_operations = sort_operation_instances(executed_operations)
    five_operations = sorted_operations[:5]
    for operation in five_operations:
        formatted_date = operation.date.strftime("%d.%m.%Y")
        masked_from = convert_payment(operation._from)
        masked_to = convert_payment(operation._to)
        print(f"{formatted_date} {operation.description}\n{masked_from} -> {masked_to}\n{operation.operation_amount['amount']} {operation.operation_amount['currency']['name']}\n\n")

if __name__ == '__main__':
    main()

