import pdfplumber

class PdfService:
    """
    Pdf service for extracting and processing data from PDF tables.
    """
    __firstRow: list[str] | None = None
        
    def extractData(self, path: str) -> list[list[str]]:
        """
            Extracts tables from a PDF file and processes all pages.
            
            :param path: Path to the PDF file
            :return list[list[str]]: List of tables with cleaned data
        """
        tables: list[list[str]] = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    tables.append(self.manipulateData(table))
        return tables
     
                    
                    
                
    
    def manipulateData(self, table: list[list[str]]) -> list[str] | None:
        """
        Cleans and processes extracted table data.
        
        :param table: Raw table data extracted from the PDF
        :return list[str]: Cleaned table data
        """
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
        