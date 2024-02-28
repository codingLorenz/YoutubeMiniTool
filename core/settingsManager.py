class Config():

    def __init__(self) -> None:
        pass

    def persistFilePath(self,targetPath:str):
        file = open("previousSelectedTargetPath.txt",'x')
        file.write(targetPath)
    
    def readFilePathFromConfig(self)->str:
        try:
            return open("previousSelectedTargetPath.txt",'r').read()
        except:
            return "empty path"