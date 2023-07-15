# Tests (copy to tests/test_user_functions.py)
import pytest
import io

from src.user_functions import *


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None


def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None


def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'


def test_get_user_name_from_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Rtse'))
    assert get_user_name_from_input() is not None


def test_get_user_name_from_input_empty_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' '))
    assert get_user_name_from_input() is None


def test_get_user_password_from_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('2skxzMB*'))
    assert get_password_from_input() is not None


def test_get_user_password_from_input_no_numbers(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('rskxzMB*'))
    assert get_password_from_input() is None


def test_get_user_password_from_input_no_special(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('rskxzMB5'))
    assert get_password_from_input() is None


def test_get_user_password_from_input_no_letters(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('333333$5'))
    assert get_password_from_input() is None


def test_get_user_password_from_input_too_short(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('2skx$4'))
    assert get_password_from_input() is None