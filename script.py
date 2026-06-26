def build_query_string(base_url, **kwargs):
    result = ''

    args_result = []

    args_list = list(kwargs.items())

    for arg in args_list:

        str_arg = f"{arg[0]}={arg[1]}"

        args_result.append(str_arg)

    joined_args = '&'.join(args_result)

    print(joined_args)

    return base_url + '?' + joined_args

print(build_query_string('https://api.weather.com/v1/forecast',city='Moscow',days=3,units= 'metric'))
print("helloworld")