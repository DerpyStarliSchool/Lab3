import employee_info as ei

def test_employee_info_by_age_20s():
    result = []
    age_lower_limit = 20
    age_upper_limit = 30
    test_arr = ["John", "Jane", "Mary"]

    result = ei.get_employees_by_age_range(age_lower_limit, age_upper_limit)

    assert (result == test_arr)

def test_employee_info_by_age_30s():
    result = []
    age_lower_limit = 30
    age_upper_limit = 40
    test_arr = ["Chloe", "Mike", "Peter"]

    result = ei.get_employees_by_age_range(age_lower_limit, age_upper_limit)

    assert (result == test_arr)

def test_calculate_average_salary():
    result = 0
    test_result = 60166

    result = ei.calculate_average_salary()

    assert (result == test_result)

def test_employee_info_by_marketing():
    result = []
    department = "Marketing"
    test_arr = ["Jane", "Mary"]

    result = ei.get_employees_by_dept(department)

    assert (result == test_arr)

def test_employee_info_by_engineering():
    result = []
    department = "Engineering"
    test_arr = ["Chloe", "Mike"]

    result = ei.get_employees_by_dept(department)

    assert (result == test_arr)

def test_employee_info_by_sales():
    result = []
    department = "Sales"
    test_arr = ["John", "Peter"]

    result = ei.get_employees_by_dept(department)

    assert (result == test_arr)