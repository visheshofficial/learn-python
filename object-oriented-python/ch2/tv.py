class TV:
    def __init__(self, brand: str):
        self._brand = brand
        self._power = False
        self._is_mutued = False
        self._channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.number_of_channels = len(self._channel_list)
        # current channel settings
        self._channel_index = 0
        # range of volume levels available
        self._VOLUME_MINIMUM = 0  # constant
        self._VOLUME_MAXIMUM = 10  # constant
        # current volume settings
        self._volume = self._VOLUME_MAXIMUM / 2

    # power on
    def power(self):
        self._power = not self._power

    # increase volume
    def volume_up(self):
        if not self._power:
            return
        if self._is_mutued:
            self._is_mutued = False  # changing the volume while muted unmutes the sound

        if self._volume < self._VOLUME_MAXIMUM:
            self._volume += 1

    # decrease volume
    def volume_down(self):
        if not self._power:
            return
        if self._is_mutued:
            self._is_mutued = False  # changing the volume while muted unmutes the sound

        if self._volume > self._VOLUME_MINIMUM:
            self._volume -= 1

    def channel_up(self):
        if not self._power:
            return
        self._channel_index += 1
        if self._channel_index > self.number_of_channels:
            self._channel_index = 0  # wrap around to the first channel

    def channel_down(self):
        if not self._power:
            return
        self._channel_index -= 1
        if self._channel_index < 0:
            self._channel_index = (
                self.number_of_channels - 1
            )  # wrap around to the top channel

    def mute(self):
        if not self._power:
            return
        self._is_mutued = not self._is_mutued

    def set_channel(self, channel):
        if not self._power:
            return
        if channel in self._channel_list:
            self._channel_index = self._channel_list[channel]

    def show_information(self):
        if not self._power:
            print(f"This is a {self._brand} TV")
            print("TV is OFF")
        else:
            print(f"This is a {self._brand} TV")
            print("TV is ON")
            print(f"Channel is : {self._channel_list[self._channel_index]}")
            if self._is_mutued:
                print(f"Volume is {self._volume} (sound is muted)")
            else:
                print(f"Volume is {self._volume}")

    # get information about current settings
    # get a specific channel


tv = TV("SAMSUNG")
tv.show_information()
tv.power()
tv.show_information()
tv.channel_up()
tv.channel_up()
tv.volume_up()
tv.volume_up()
tv.show_information()
tv.power()
tv.show_information()
tv.power()
tv.show_information()
