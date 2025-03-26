import zipfile
import os

class ZipService:
    def compactCsv(file: str) -> bool:
        outDir = os.path.dirname(file)
        zipPath = os.path.join(outDir, "Teste_Vinicius_Mattera.zip")
        try:
            with zipfile.ZipFile(zipPath, "w") as fileZip:
                fileZip.write(file, arcname="Output.csv")
            return True
        except Exception as e:
            raise e