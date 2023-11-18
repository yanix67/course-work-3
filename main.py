from src.utils import load_operation, get_operation_instances, sort_operation_instances


def get_executed_operations(operations_instances):
    pass


def main():
    operations = load_operation("src/data/operations.json")
    operations_instances = get_operation_instances(operations)
    executed_operations = get_executed_operations(operations_instances)
    sorted_operations = sort_operation_instances(executed_operations)
    five_operations = sorted_operations[:5]
    for operation in five_operations:
        print(operation)
        print()


if __name__ == '__main__':
    main()