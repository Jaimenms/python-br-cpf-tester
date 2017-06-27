A test implementation of the Brazilian CPF Validation (WTTD training)
=================================================================

This is a test implementatipon of the Brazilian CPF Validation as part of
the "Mão na Massa" proposal of the 4th module of Welcome to the Django
training (http://welcometothedjango.com.br/).

CPF is a document that identifies a taxpayer at the Federal Internal Revenue
Department. The CPF carries registration information supplied by the
individual and by the Federal Internal Revenue Department database.

This number is currently formated as XXX.XXX.XXX-DD where X are digits and D
are check digits.

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.6.
3. Ative o virtualenv.
4. Instale as dependências
5. Execute os testes

```console
git clone git@github.com:jaimenms/python-br-cpf-tester.git python brcpf
cd brcpf
python -m venv .brcpf
source .brcpf/bin/activate
pip install -r requirements.txt
pytest
```

## Como utilizar?

1. Instale o pacote
2. Execute o módulo

```console
pip install braziliancpftests
import brcpftester
python brcpftester.py
