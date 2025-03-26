import csv
import os

class CsvService:
    def saveToCsv(tables: list[list[str]]) -> tuple[bool, str]:
        try:
            
            baseDir = os.path.dirname(os.path.abspath(__file__))
            filePath = os.path.join(baseDir, "../../data", "output.csv")
            with open(filePath, mode="w+", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file, delimiter=";")
                for table in tables:
                    for row in table:
                        writer.writerow(row)
            return True, filePath 
        except Exception as e:
            raise e     