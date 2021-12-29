import os


class Services:

    def pwd():
        f = os.popen('pwd')
        r = f.read()
        return r

    def env():
        env = dict(os.environ)
        return env

    def printenv():
        f = os.popen('printenv')
        r = f.read()
        return r

    def create_env(env_name, env_v):
        if str(env_name).isupper() == False:
            env_name = str(env_name).upper()
        os.environ[str(env_name)] = str(env_v)
        f = os.popen("bash -c 'echo $%s'" % env_name)
        r = f.read()
        return "new env_var %s=" % env_name + r

    def running_software():
        f = os.popen("ps aux")
        r = f.read()
        return r

    def specific_running_software(serv_name):
        f = os.popen("ps aux | grep %s" % serv_name)
        r = f.read()
        return r
        