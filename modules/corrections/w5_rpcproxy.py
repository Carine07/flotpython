# @BEG@ 5 6 RPCProxy
# une troisi�me impl�mentation de RPCProxy

class Forwarder(object):
    def __init__(self, rpc_proxy, function):
        self.function = function
        self.rpc_proxy = rpc_proxy
    # en rendant cet objet callable, on peut l'utiliser
    # comme m�thode dans RPCProxy
    def __call__(self, *args):
        print "Envoi � {}\nde la fonction {} -- args= {}".\
            format(self.rpc_proxy.url, self.function, args)
        return "retour de la fonction " + self.function

class RPCProxy(object):
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__ (self, function):
        """
        Cr�e � la vol�e une instance de Forwarder
        correspondant � 'function'
        """
        return Forwarder(self, function)

# @END@
