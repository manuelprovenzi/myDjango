import csv

class SerializerCSV:
    def __init__(self,nomeFile):
        self.fileCsv = open(nomeFile,"rt")
        self.listString = list()
        self.listProvince = list()
        self.Serialize()
    def Serialize(self):
        iteratorRow = csv.reader(self.fileCsv)
        next(iteratorRow)
        try:
            for row in iteratorRow:
                strRow = row.__str__()
                strRowSplitted = strRow.split(";")
                name =  strRowSplitted[5]
                provincia =  strRowSplitted[11]
                if name=='-' or provincia=='-':
                    continue

                self.listString.append(name)
                self.listProvince.append(provincia)
        except UnicodeDecodeError as e:
            return None

        return 1
