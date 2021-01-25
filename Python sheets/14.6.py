class Converter:
    units=['inches', 'feet', 'yards', 'miles', 'kilometers', 'meters', 'centimeters', 'millimeters']

    def __init__(self,length,unit):
        self.length=length
        self.unit=unit

        if self.unit=='inches':
            self.inches()
        elif self.unit=='feet':
            self.feet()
        elif self.unit=='yards':
            self.yards()
        elif self.unit=='miles':
            self.miles()
        elif self.unit=='kilometers':
            self.kilometers()
        elif self.unit=='meters':
            self.meters()
        elif self.unit=='centimeters':
            self.centimeters()
        elif self.unit=='millimeters':
            self.millimeters()


    def inches(self):
        print(self.length,self.units[0])

    def feet(self):
        print(self.length,self.units[1])

    def yards(self):
        print(self.length,self.units[2])

    def miles(self):
        print(self.length,self.units[3])

    def kilometers(self):
        print(self.length,self.units[4])

    def meters(self):
        print(self.length,self.units[5])

    def centimeters(self):
        print(self.length,self.units[6])

    def millimeters(self):
        print(self.length,self.units[7])


c=Converter(150,'feet')

