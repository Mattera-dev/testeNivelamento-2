from services.pdfService import PdfService
from services.csvService import CsvService

pdfService = PdfService()

def main():
    data = pdfService.extractData("./data/Anexo I.pdf")
    suce, file = CsvService.saveToCsv(data)

if __name__ == "__main__":
    main()