from time import sleep

def retry(times):
    print(f"Retrying... {times}")
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper
    return decorator

@retry(3)
def open_site(url):
    print(f"Oenning site: {url}")
    sleep(2)

open_site("https://www.google.com")