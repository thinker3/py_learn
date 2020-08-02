
import inspect
def get_source_code(obj):
    code = inspect.getsource(obj)
    return code

def get_methods(obj, t=(0,)):
    members = inspect.getmembers(obj)
    all_methods = []
    for one in members:
        if inspect.ismethod((one[1])):
            all_methods.append(one)

    methods = []
    for one in all_methods:
        if not one[0].startswith('_'):
                methods.append(one)

    methods__ = []
    for one in all_methods:
        if one[0].startswith('__'):
            methods__.append(one)

    for one in methods__ + methods:
        all_methods.remove(one)
    methods_ = all_methods
    all_methods = [methods, methods_, methods__]
    temp = []
    for i in t:
        temp += all_methods[i]
    return temp


    
def get_non_methods(obj):
    members = inspect.getmembers(obj)
    non_methods = []
    for one in members:
        if not inspect.ismethod((one[1])):
            non_methods.append(one)
    return non_methods



if __name__ == "__main__":
    import mechanize
    br = mechanize.Browser
    code = get_source_code(br)
    code = get_source_code(br.select_form)
    code = get_source_code(br()._factory.forms)
    non_methods = get_non_methods(br)
    for one in non_methods:
        print(one)
    code = get_source_code(br.click)
    code = get_source_code(mechanize.HTMLForm.click)
    #print code
