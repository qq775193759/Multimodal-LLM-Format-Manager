import json
from dataclasses import dataclass
from types import SimpleNamespace


def seq_parser(seq_str):
    seq_list = seq_str.split(' ')
    cleaned_seq_list = list(filter(None, seq_list))
    return seq_list
    
def variable_parser(variable):
    variable_name = variable
    variable_type = 'list'
    return variable_name, variable_type

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
            
    def format_frame_data(self, data, video_idx, frame_idx):
        frame_data = {}
        for role in self.data_format:
            variables = self.data_format[role]
            content_list = []
            for variable in variables:
                variable_name, variable_type = variable_parser(variable)
                if variable_type == 'list':
                    content_data = data[variable_name][video_idx][frame_idx]
                if variable_type == 'element':
                    content_data = data[variable_name][video_idx]
                content_list.append(content_data)
            frame_data[role] = content_list
        return frame_data
        
    def format_video_data(self, data, video_idx):
        pass

    def format_all_data(self, data):
        pass



