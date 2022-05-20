from datetime import datetime

def log_it(path):
    def _log_it(function):
        def _new_log_it(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(path, 'a') as file:
                file.write(f"Дата и время запуска функции {function.__name__}: {datetime.now().strftime('%A, %d %B %Y %H:%M:%S')}"
                           f"с результатом {result}\n")
            return result

        return _new_log_it

    return _log_it