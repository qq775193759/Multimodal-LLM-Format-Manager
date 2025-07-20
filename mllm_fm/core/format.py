import json
from dataclasses import dataclass
from types import SimpleNamespace


def seq_parser(seq_str):
    seq_list = seq_str.split(' ')
    cleaned_seq_list = list(filter(None, seq_list))
    return seq_list
    

class FormatBase:
    def __init__(self, data_format):
        isinstance(data_format, str):
            data_format = json.loads(data_format)
            
        self.data_format = {}
        for key in data_format:
            value = data_format[key]
            isinstance(value, str):
                value = seq_parser(value)
            self.data_format[key] = value





