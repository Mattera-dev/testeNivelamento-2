import pdfplumber

class PdfService:
    __firstRow: list[str] | None = None
        
    def extractData(self, path: str) -> list[list[str]]:
        tables: list[list[str]] = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    tables.append(self.manipulateData(table))
                    break
        return tables
     
                    
                    
                
    
    def manipulateData(self, table: list[list[str]]) -> list[str] | None:
        tableCleaned = []
        for row in table:
            if self.__firstRow == row:
                continue
            if not self.__firstRow:
                self.__firstRow = row
            rowCleaned = []
            for cell in row:
                cellClean = cell.replace("\n", " ").strip()
                match cellClean:
                    case "OD":
                        cellClean = "Seg. Odontologico"
                    case "AMB":
                        cellClean = "Seg. Ambulatorial"
                rowCleaned.append(cellClean)
                        

            if any(rowCleaned):
                tableCleaned.append(rowCleaned)
        return tableCleaned
        