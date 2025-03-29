import zipfile
import os

class ZipService:
    """
    Zip service for compacting files in .zip
    """
    @staticmethod
    def compactCsv(File: str) -> bool:
        """
        Compact the file to a .zip in the '/data' folder
        
        :param File: Path to csv file
        :return bool: true if success, raises exception if error
        """
        outDir = os.path.dirname(File)
        zipPath = os.path.join(outDir, "Teste_Vinicius_Mattera.zip")
        try:
            with zipfile.ZipFile(zipPath, "w") as fileZip:
                fileZip.write(File, arcname="Output.csv")
            return True
        except Exception as e:
            raise e