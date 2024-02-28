from downloader import Downloader
from settingsManager import Config

def main():
    config = Config()
    path:str = input(f"Specify the target directory (current: \"{config.readFilePathFromConfig()}\"): ")
    if(isPathEmpty(path)):
        path=config.readFilePathFromConfig()
    else:
        config.persistFilePath(targetPath=path)
    
    downloader = Downloader(
       sourceURL=input("Specify a Youtube URL to download (single Video or Playlist): "),
       outputPath=path 
    )
    downloader.downloadAudio()
    print("Done! :)")

def isPathEmpty(path:str):
    return len(path.strip())<=0

if __name__ == '__main__':
    main()