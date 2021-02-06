import requests

class Dynamic_Execution:
    @classmethod
    def __init__(cls, url):
        cls.script = requests.get(url).text
    
    @classmethod
    def function_definition(cls, function_def):
        function_def = function_def.replace("{}", '"{}"')
        cls.function_def = function_def
        return cls

    @classmethod
    def exec(cls, *args):
        local_env = {}
        final_func = cls.function_def.format(*args)
        final_func = final_func.replace("\\", '\\\\')
        d = dict(local_env, **globals())
        exec(cls.script + "\n\n" + final_func + "\n", d, d)
        print(local_env)

        return cls


url = "https://raw.githubusercontent.com/justindd1994/Dynamic_Python/master/SetFolderIcon.py"
dynamic_func = Dynamic_Execution(url).function_definition("SetFolderIcon({}, {})")
dynamic_func.exec("D:\\General\\", "D:\\General\\Title.ico")
