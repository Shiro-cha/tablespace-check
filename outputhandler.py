class OutputHandler:
    def __init__(self, output):
        self.output = output
    def parse(self):
        start="options\n"
        end="rows selected"
        tablestring=self.substring(start,end)
        self.filterheader('-').filterheader("Tablespace").filterheader("Total Size(MB) Free Size(MB)").filterheader("%Free").filterheader("                     ").filterheader("\n    % Used").filterheader("\n        ")
        
        return self.output;

    def substring(self,start, end):
        start_index = self.output.find(start) + len(start)
        end_index = self.output.find(end) - 4
        result= self.output[start_index+1:end_index]
        self.output = result;
    

    def filterheader(self,header):
        withoutheader=self.output.replace(header,"")
        self.output=withoutheader;
        return self
        