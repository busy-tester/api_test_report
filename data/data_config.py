class global_var:

    Id = 1
    requestName = 2
    api_name = 3
    run = 4
    url = 7
    header = 8
    request_way = 9
    data = 10
    http_code = 11
    expect = 12
    result = 13
    run_time = 14
    error_msg = 15
    depend_value = 16
    set_depend_key = 17
    waiting_replace_key = 18
    actual_replace_key = 19
    case_depend = 26
    data_depend = 27
    field_depend = 28


def get_id():
    return global_var.Id


def get_request_name():
    return global_var.requestName


def get_api_name():
    return global_var.api_name


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_run_way():
    return global_var.request_way


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


def get_data():
    return global_var.data


def get_expect():
    return global_var.expect


def get_http_code():
    return global_var.http_code


def get_result():
    return global_var.result


def get_run_time():
    return global_var.run_time


def get_error_msg():
    return global_var.error_msg

#提取的值


def get_depend_value():
    return global_var.depend_value


def get_set_key():

    return global_var.set_depend_key


def get_waiting_replace_key():
    return global_var.waiting_replace_key


def get_actual_replace_key():
    return global_var.actual_replace_key


def get_header_value():
    header = {
        "x-test-case":"134f08ad5b9b40c2af4324d2767fde35",
        "x-api-key":"54b99190163e0f39e23b6707a89c80fb",
        "x-api-signature":"6778",
        "Content-Type":"application/json",
        "x-noauth":"true"
    }

    return header









