numero = 123
titular = "EDUARDO"
saldo = 100.0
limit = 1000.0

##conta = {"numero":123,"titular":"EDUARDO",
##        "saldo":100.0,"limite":1000.0
##}

##print(conta["titular"])
##print(conta["limite"])

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero":numero,"titular":titular,
            "saldo":saldo,"limite":limite
    }
    return conta

conta = criar_conta(345, "EDUARDO", 100.0, 1000.0)
print(conta)

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"seu saldo atual é {conta["saldo"]}")

depositar(conta, 300.0)
extrato(conta)
sacar(conta, 250.0)
extrato(conta)
