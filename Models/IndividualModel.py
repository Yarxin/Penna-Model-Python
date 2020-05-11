class Individual:

    def __init__(self):
        self.__chromatine1 = []
        self.__chromatine2 = []
        self.__genotype = [self.__chromatine1, self.__chromatine2]
        self.__T = 0
        self.__age = 0
        self.__procreation_age = 0
        self.__sex = 0

    @property
    def Genotype(self):
        return self.__genotype

    @Genotype.setter
    def Genotype(self, value):
        self.__genotype = value

    @property
    def Chromatine1(self):
        return self.__chromatine1

    @Chromatine1.setter
    def Chromatine1(self, value):
        self.__chromatine1 = value

    @property
    def Chromatine2(self):
        return self.__chromatine2

    @Chromatine2.setter
    def Chromatine2(self, value):
        self.__chromatine2 = value

    @property
    def T(self):
        return self.__T

    @T.setter
    def T(self, value):
        self.__T = value

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        self.__age = value

    @property
    def Procreation_age(self):
        return self.__procreation_age

    @Procreation_age.setter
    def Procreation_age(self, value):
        self.__procreation_age = value

    @property
    def Sex(self):
        return  self.__sex

    @Sex.setter
    def Sex(self, value):
        self.__sex = value
