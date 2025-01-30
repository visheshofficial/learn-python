class DimmerSwitch:
    def __init__(this):
        this._is_on = False
        this._brightness = 0

    def turn_on(this):
        this._is_on = True

    def turn_off(this):
        this._is_on = False

    def raise_level(this):
        this._brightness += 1

    def lower_level(this):
        this._brightness -= 1

    def display_status(this):
        print(f"The Dimmer Switch is {'on' if this._is_on else 'off'}")
        print(f"The brightness level is {this._brightness}")


dimmer_switch = DimmerSwitch()
dimmer_switch.turn_on()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.display_status()

dimmer_switch.lower_level()
dimmer_switch.lower_level()
dimmer_switch.turn_off()
dimmer_switch.display_status()

dimmer_switch.turn_on()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.raise_level()
dimmer_switch.display_status()

print(type(dimmer_switch))
print(vars(dimmer_switch))
# print(vars(DimmerSwitch))
