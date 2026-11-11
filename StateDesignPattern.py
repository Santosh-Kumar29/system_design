# Music Player

# Design a music player with these states:

# Stopped
# Playing
# Paused


from abc import ABC, abstractmethod

class MusicPlayer(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def pause(self):
        pass

class PlayingState(MusicPlayer):
    def start(self):
        print("Playing music")

    def stop(self):
        print("Stopping music")

    def pause(self):
        print("Pausing music")

class PausedState(MusicPlayer):
    def start(self):
        print("Playing music")

    def stop(self):
        print("Stopping music")

    def pause(self):
        print("Pausing music")

class StoppedState(MusicPlayer):
    def start(self):
        print("Playing music")

    def stop(self):
        print("Stopping music")

    def pause(self):
        print("Pausing music")

class MusicPlayerContext:
    def __init__(self):
        self.state = StoppedState()

    def start(self):
        self.state.start()

    def stop(self):
        self.state.stop()

    def pause(self):
        self.state.pause()