import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("[LOG] Method calculate_performance() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(is_admin, *args, **kwargs):
        if not is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(is_admin, *args, **kwargs)
    return wrapper
