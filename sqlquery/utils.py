from django.db import connection


def log_queries(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        for query in connection.queries:
            _sql = query['sql']
            _time = query['time']
            print(f'QUERY: {_sql.replace("", "")}\nTIME: {_time}s\n\n')
        return response
    return wrapper
