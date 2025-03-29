from services.pdfService import PdfService
from services.csvService import CsvService
from services.zipService import ZipService

pdfService = PdfService()

def main():
    data = pdfService.extractData("./data/Anexo I.pdf")
    err, file = CsvService.saveToCsv(data)
    if not err:
        if ZipService.compactCsv(file): 
            print("O arquivo foi zipado com sucesso!")
    else:
        print("Failed saving tables in csv file")

if __name__ == "__main__":
    main()