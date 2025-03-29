import csv
import os

class CsvService:
    """
    CSV service for saving data to .csv
    """
    @staticmethod
    def saveToCsv(tables: list[list[str]]) -> tuple[bool, str]:
        """
        Save the provided data to a .csv file in the '/data' folder
        
        :param tables: List of tables containing rows of data
        :return tuple[bool, str]: True and csv file path if success, raises exception if error
        """
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