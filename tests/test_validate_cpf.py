# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import pytest
from brcpftester import BrazilianCpfValidationTests


def test_success():

    cpf = BrazilianCpfValidationTests()

    casos = [
        '123.456.789-09',
        '12345678909',
    ]

    for caso in casos:
        cpf(caso)
        assert not cpf.tests


def test_checkdigits():

    cpf = BrazilianCpfValidationTests()

    casos = [
        '123.456.789-19',
        '12345678919',
    ]

    for caso in casos:
        cpf(caso)
        assert 'checkdigits' in cpf.tests

def test_length():

    cpf = BrazilianCpfValidationTests()

    casos = [
        '1234',
        '123456789012',
    ]

    for caso in casos:
        cpf(caso)
        assert 'length' in cpf.tests

def test_digits():

    cpf = BrazilianCpfValidationTests()

    casos = [
        'ABCD5678901',
        '1234567ABCD',
    ]

    for caso in casos:
        cpf(caso)
        assert 'digits' in cpf.tests

def test_charformat():

    cpf = BrazilianCpfValidationTests()

    casos = [
        '123456789-01',
        '123.456.78901',
        '123.456.789.01',
    ]

    for caso in casos:
        cpf(caso)
        assert 'charformat' in cpf.tests
