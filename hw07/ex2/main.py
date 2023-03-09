# печать таблицы по заданной функции
def print_operation_table(operation, num_rows, num_columns):
    for x in range(1, num_columns+1):
        for y in range(1, num_rows+1):
            print(operation(x,y), end ='  ')
        print()
print_operation_table(lambda x,y: x*y,6,6)