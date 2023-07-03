from abc import ABC, abstractmethod
from string import Template
import re


def tokens_to_str(*tokens):
    tokens = filter(bool, tokens)
    tokens = map(lambda t: str(t), tokens)
    tokens = filter(bool, tokens)

    return " ".join(tokens) if tokens else ""

def stringify(str_or_list: str | list[str]):
    if isinstance(str_or_list, str):
        str_or_list = [str_or_list]
    return tokens_to_str(*str_or_list)

def listify(str_or_list: str | list[str]):
    if not isinstance(str_or_list, list):
        str_or_list = [str_or_list]
    return str_or_list

def run_partial_templates(
    template_strings: list[str], template_args: dict
) -> list[str]:
    template_args = {k: ("" if v is None else v) for k, v in template_args.items()}
    return [Template(t).safe_substitute(template_args) for t in template_strings]
