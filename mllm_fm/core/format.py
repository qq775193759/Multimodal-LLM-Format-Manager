import json
import re


def seq_parser(seq_str):
    seq_list = seq_str.split(' ')
    cleaned_seq_list = list(filter(None, seq_list))
    return seq_list
    
def variable_parser(expr, frame_idx):
    indexed_match = re.fullmatch(r"^([a-zA-Z_]\w*)\[([^\]]+)\]$", expr)
    if indexed_match:
        name = indexed_match.group(1)
        index_expr = indexed_match.group(2)
        index_expr = index_expr.format(i = frame_idx)
        return name, [eval(index_expr)]
    else:
        return expr, []

class FormatBase:
    def __init__(self, data_format):
        if isinstance(data_format, str):
            data_format = json.loads(data_format)
            
        self.data_format = {}
        for key in data_format:
            value = data_format[key]
            if isinstance(value, str):
                value = seq_parser(value)
            self.data_format[key] = value
            
    def format_frame_data(self, data, video_idx, frame_idx):
        frame_data = {}
        for role in self.data_format:
            variables = self.data_format[role]
            content_list = []
            for variable_str in variables:
                variable_name, frame_idxs = variable_parser(variable_str, frame_idx)
                for frame_idx in frame_idxs:
                    if frame_idx < 0:
                        continue
                    content_list.append(data[variable_name][video_idx][frame_idx])
                if len(frame_idxs) == 0:
                    content_list.append(data[variable_name][video_idx])
            frame_data[role] = content_list
        return frame_data
        
    def format_video_data(self, data, video_idx):
        pass

    def format_all_data(self, data):
        pass

if __name__ == '__main__':
    a = {'input':'task data[{i}-1] data[{i}]'}
    data = {'data':[[1,2,3]], 'task':['a','b']}
    af = FormatBase(a)
    print(af.format_frame_data(data, 0, 0))