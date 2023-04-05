from first_class import FirstClass
from second_class import SecondClass
from third_class import ThirdClass
from database import Database


def main():
    fc = FirstClass()
    sc = SecondClass()
    tc = ThirdClass()

    fc.database.data.append('primeira mudança')
    sc.database.data.append('segunda mudança')
    tc.database.data.append('terceira mudança')

    fc_test = isinstance(fc.database, Database)
    sc_test = isinstance(sc.database, Database)
    tc_test = isinstance(tc.database, Database)

    fc_database = id(fc.database)
    sc_database = id(sc.database)
    tc_database = id(tc.database)

    fc_two_database = id(fc.instance_database)
    sc_two_database = id(sc.instance_database)
    tc_two_database = id(tc.instance_database)

    print(fc_test, sc_test, tc_test)
    print(fc_database, sc_database, tc_database)
    print(fc_two_database, sc_two_database, tc_two_database)
    print(fc.database.data, sc.database.data, tc.database.data)


if __name__ == '__main__':
    main()
