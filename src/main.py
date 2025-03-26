from services.pdfService import PdfService

pdfService = PdfService()

def main():
    data = pdfService.extractData("./data/Anexo I.pdf")

if __name__ == "__main__":
    main()