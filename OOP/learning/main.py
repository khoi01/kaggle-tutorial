

from abc import ABC, abstractmethod


class Exported(ABC):
    @abstractmethod
    def export(self,data):
        pass

class PDFExporter(Exported):
    def export(self,data):
        return f"Exported {data} as PDF"
    
class CSVExporter(Exported):
    def export(self, data):
        return f"Exported {data} as CSV"

def run_export(exported:Exported,data:str):
    print(exported.export(data))




def main():
    pdf = PDFExporter()
    csv = CSVExporter()
    
    run_export(pdf,"Report")
    run_export(csv,"Invoice")





if __name__ == '__main__':
    main()

