class Time:
    def __init__(self,seconds):
        self.seconds = seconds

    def convert_to_minutes(self, seconds):
        if seconds >= 60 or seconds == 0:
            return '%02d:%02d' % (seconds / 60, seconds % 60)
        else:
            return '00:%02d' % (seconds)

    def convert_to_hours(self, seconds):
        if seconds >= 60 * 60 or seconds == 0:
            return '%02d:' % (seconds / (60 * 60)) + self.convert_to_minutes(seconds % (60 * 60))

        else:
            return '%02d' % seconds


time = Time(120)
print(time.convert_to_minutes(59))
print(time.convert_to_hours(3660))
