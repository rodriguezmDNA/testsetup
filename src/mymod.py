def aggnums(a, b):
    try:
        if a is None or b is None:
            print('need a or b')
            raise
        else:
            return (a+b)

    except:
        return None


def validateIPregex(ip):
    import re
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
        return True
    else:
        return False
