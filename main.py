import inspect
import pprint
import test


def get_type(obj) -> str:
    '''Возвращает только тип объекта, использцется в introspection_info(obj)'''
    dict_type = {'type': 'Класс', 'function': 'Функция', 'module': 'Модуль'}
    if str(type(obj)).split("'")[1] in dict_type:
        return dict_type[str(type(obj)).split("'")[1]]
    else:
        return str(type(obj)).split("'")[1]


def get_heir(obj, str_class) -> str:
    '''Возвращает предка класса используется в introspection_info(obj)'''
    cls = getattr(obj, str_class)
    heir = str(inspect.getmro(cls)).split("'")[3]
    return heir


# def bool_elem(x, y) -> bool:
#     return True if x == y else False


def introspection_info(obj) -> list:
    '''Возвращает список всех данных объекта'''
    try:
        obj_name = obj.__name__
    except:
        obj_name = 'Объект'
    obj_type = get_type(obj)

    my_all = [element[0] for element in inspect.getmembers(obj) if not element[0].startswith(('_', '__'))]
    my_modules = [name_module[0] for name_module in inspect.getmembers(obj, predicate=inspect.ismodule)]
    my_classes = {name_class[0]: get_heir(obj, name_class[0]) for name_class in
                  inspect.getmembers(obj, predicate=inspect.isclass) if not name_class[0].startswith(('_', '__'))}

    my_functions = [name_fun[0] for name_fun in inspect.getmembers(obj, predicate=inspect.isfunction) if
                    not name_fun[0].startswith(('_', '__'))]

    my_var = [x for x in my_all if x not in (my_modules + list(my_classes.keys()) + my_functions)]

    return [obj_name, obj_type, my_modules, my_classes, my_functions, my_var, obj]


def show_modules(list_modules) -> None:
    if len(list_modules) > 0:
        print('МОДУЛИ:')
        tmp = 'Модуль'
        count = 1
        for m in list_modules:
            print(f'{count}. {tmp:<25}{m}')
            count += 1
    print('')


def show_class(dict_class) -> None:
    if len(dict_class) > 0:
        print('КЛАССЫ:')
        count = 1
        for key, value in dict_class.items():
            print(f'{count}. {key:<25}наследуется от {value}')
            count += 1
    print('')


def show_fun(list_functions, type_obj) -> None:
    tmp = ['Метод', 'Функция']
    print('ФУНКЦИИ:')
    count = 1
    if len(list_functions) > 0:
        for fun in list_functions:
            if type_obj == 'Класс':
                print(f'{count}. {tmp[0]:<24}{fun}()')
            else:
                print(f'{count}. {tmp[1]:<24} {fun}()')
            count += 1
    print('')


def show_var(list_var, obj):
    tmp = ['Объект', 'класса']
    print('ПЕРЕМЕННЫЕ:')
    count = 1
    if len(list_var) > 0:
        for var in list_var:
            cls = getattr(obj, var)
            print(f'{count}. {tmp[0]} {var:<15}   {tmp[1]} {str(type(cls)).split("'")[1]}')
            count += 1


def show_obj(obj) -> None:
    print(f'Имя объекта - {obj[0]:<5} тип - {obj[1]:<5}')
    print('Включает в себя:')
    show_modules(obj[2])
    show_class(obj[3])
    show_fun(obj[4], obj[1])
    show_var(obj[5], obj[6])

show_obj(introspection_info(inspect))
show_obj(introspection_info(test))

z = 1
