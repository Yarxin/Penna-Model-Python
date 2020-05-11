from Models.IndividualModel import Individual
import random


class IndividualFactory:

    def CreatePopuation(self, number_of_genes, number_of_individs, param_T, procreation_age):
        population = []
        i = 0
        while(i < number_of_individs):
            individual = self.__Create(number_of_genes, param_T, procreation_age)
            population.append(individual)
            i += 1
        return population

    def __Create(self, number_of_genes, param_T, procreation_age):
        individual = Individual()
        individual.Genotype = []
        i = 0
        while(i < number_of_genes):
            rnd_1 = random.randint(0, 1)
            individual.Chromatine1.append(rnd_1)
            rnd_2 = random.randint(0, 1)
            individual.Chromatine2.append(rnd_2)
            individual.T = param_T
            individual.Procreation_age = procreation_age
            individual.Age = random.randint(1, number_of_genes)
            individual.Sex = random.randint(0, 1)
            i += 1
        return individual
