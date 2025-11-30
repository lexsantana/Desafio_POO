# tests/test_conta.py
import pytest
from Resolucao_desafio_poo import ContaCorrente, PessoaFisica, Deposito, Saque

def test_deposito_e_saldo():
    cliente = PessoaFisica("Teste", "01-01-2000", "00000000000", "Rua X")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=1)
    dep = Deposito(100.0)
    dep.registrar(conta)
    assert conta.saldo == pytest.approx(100.0)

def test_saque_sucesso():
    cliente = PessoaFisica("Teste", "01-01-2000", "00000000001", "Rua X")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=2)
    conta.depositar(200.0)
    s = Saque(50.0)
    s.registrar(conta)
    assert conta.saldo == pytest.approx(150.0)

def test_saque_excede_saldo():
    cliente = PessoaFisica("Teste", "01-01-2000", "00000000002", "Rua X")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=3)
    conta.depositar(50.0)
    s = Saque(100.0)
    s.registrar(conta)
    # saldo deve continuar 50
    assert conta.saldo == pytest.approx(50.0)
