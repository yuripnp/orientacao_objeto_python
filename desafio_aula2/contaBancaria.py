class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self._titular = titular
        self._numero_conta = numero_conta
        self._saldo = 0.0
        self._extrato = []
        self._ativo = False
    

    def __str__(self):
        return f"ContaBancaria(titular={self._titular}, numero_conta={self._numero_conta}, saldo={self._saldo})"
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def numero_conta(self):
        return self._numero_conta
    

    def ativar_conta(self):
        self._ativo = True
        print(f"Conta {self._numero_conta} ativada.")
        self._extrato.append(f"Conta {self._numero_conta} ativada.")
    

    
