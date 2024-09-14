from django.conf import settings
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format


def log_queries(func):
    def wrapper(*args, **kwargs):
        """
        connection.queries is only available if DEBUG is True        """
        response = func(*args, **kwargs)
        duplicate_queries = set()

        for query in connection.queries:
            _sql = query['sql']
            _time = query['time']
            _sql_formatted = format(str(_sql), reindent=True)
            _sql_pretty_formatted = highlight(
                _sql_formatted, SqlLexer(), TerminalFormatter())
            _time_pretty_formatted = highlight(
                f'{_time}s', SqlLexer(), TerminalFormatter()
            )

            duplicate_queries.add(_sql)
            print(
                f'Query: {_sql_pretty_formatted}Time: {_time_pretty_formatted}', end="")
        if settings.DEBUG:
            q_count = len(connection.queries)
            d_count = q_count - len(duplicate_queries)

            query_count = highlight(
                f'Total Queries: {q_count}', SqlLexer(), TerminalFormatter())
            duplicate_count = highlight(
                f'Duplicate Queries: {d_count}', SqlLexer(), TerminalFormatter())

            print(query_count, end="")
            print(duplicate_count)
        return response
    return wrapper
