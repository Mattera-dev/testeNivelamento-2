from services.pdfService import PdfService
from services.csvService import CsvService
from services.zipService import ZipService

pdfService = PdfService()

def main():
    data = pdfService.extractData("./data/Anexo I.pdf")
    suce, file = CsvService.saveToCsv(data)
    if suce:
        if ZipService.compactCsv(file): 
            print("O arquivo foi zipado com sucesso!")
    else:
        print("Failed saving tables in csv file")

if __name__ == "__main__":
    main()