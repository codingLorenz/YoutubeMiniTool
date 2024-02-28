from pytube import YouTube,Stream,Playlist
import os,shutil


class Downloader():
    
    def __init__(self,sourceURL,outputPath):
        self.sourceURL = sourceURL
        self.outputPath = outputPath


    def getHighestBitrateStream(self,streams:list[Stream])-> Stream: 
        return max(streams, key=lambda stream:stream.bitrate)

    def getOpusStreamsFromYoutubeVideo(self,ytVideo:YouTube)->list[Stream]:
        return ytVideo.streams.filter(only_audio=True,audio_codec="opus")

    def isPlaylist(self)->bool:
        return "list=" in self.sourceURL
    
    def cleanStringForFilename(self,input:str):
        return ''.join(letter for letter in input if letter.isalnum())
    

    def downloadeSingleAudio(self,ytVideo:YouTube,outputPath:str):
        opusStreams = self.getOpusStreamsFromYoutubeVideo(ytVideo=ytVideo)
        maxQualityOpusStream = self.getHighestBitrateStream(opusStreams)
        maxQualityOpusStream.download(
            output_path = outputPath,
            filename = self.cleanStringForFilename(maxQualityOpusStream.title)+"."+maxQualityOpusStream.audio_codec
        )

    def downloadPlaylistAudios(self,ytPlaylist:Playlist):
      playlistFolderPath = self.outputPath+"\\"+ytPlaylist.title
      if(os.path.exists(playlistFolderPath)):
          shutil.rmtree(playlistFolderPath)
      os.makedirs(playlistFolderPath)
      for video in ytPlaylist.videos:
            print("Downloading "+video.title)
            self.downloadeSingleAudio(video,playlistFolderPath)
   
    
    def downloadAudio(self):
        if(self.isPlaylist()):
            ytPlaylist = Playlist(self.sourceURL)
            self.downloadPlaylistAudios(ytPlaylist)
        else:
            ytVideo = YouTube(self.sourceURL)
            self.downloadeSingleAudio(ytVideo,self.outputPath)