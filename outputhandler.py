import re
class OutputHandler:
    def __init__(self, output):
        self.output = output

    def parse(self):
        parsed_output = self._substring("options\n", "rows selected")
        parsed_output = self._filter_headers(parsed_output)
        parsed_lines = self._divide_by_line(parsed_output)
        byspaces = self._divide_by_space_and_trim(parsed_lines)
        result = self.create_dict(byspaces)
        return result

    def _substring(self, start, end):
        start_index = self.output.find(start) + len(start)
        end_index = self.output.find(end) - 4
        return self.output[start_index + 1:end_index]

    def _filter_headers(self, output):
        headers_to_remove = [
            '-',
            'Tablespace',
            'Total Size(MB) Free Size(MB)',
            '%Free',
            '                     ',
            '\n    % Used',
            '\n        '
        ]
        for header in headers_to_remove:
            output = output.replace(header, "")
        return output

    def _divide_by_line(self, output):
        return output.split("\n")

    def _divide_by_space_and_trim(self, lines):
        result = [re.split(r" +|\t+", line) for line in lines if line.strip()]
        
        for i,line in enumerate(result):
            line = [x for x in line if x]
            for j,element in enumerate(line):
                result[i][j] = element.strip()
            
            if len(line) == 1:
                result[i-1].append(line[j])
                result[i-1] = [x.strip() for x in result[i-1]]
                result.pop(i)

        
        result=[[item for item in line if item] for line in result]

        return result;
    def create_dict(self,byspaces):
        dicts = [] 
        headers = ["Tablespace", "Total Size(MB)", "Free Size(MB)", "%Free", "% Used"]
        
        for byspace in byspaces:
            # print the length of the list
            #print(len(byspace), " ".join(byspace))
            if len(byspace) != len(headers):
                continue
            for j,element in enumerate(byspace):
                
                dicts.append({headers[j]:element})

        return dicts
        