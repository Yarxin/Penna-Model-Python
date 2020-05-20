from Models.IndividualModel import Individual
import random


class GeneticOperationService:

    def MutateIndividual(self, individual):
        self.__Mutate(individual)
        return individual

    def CrossingOverIndividual(self, individual):
        self.__CrosingOver(individual)
        return individual

    def ReplicateIndividual(self, gametes_father, gametes_mother):
        individual = self.__Replicate(gametes_father, gametes_mother)
        return individual

    def GametesCreationIndividual(self, individual):
        self.__GametesCreation(individual)
        return individual

    def __Mutate(self, individual):

        M = 0.03
        for gen in individual.Chromatine1:
            rnd = random.randint(1, 33) #3% na mutację
            if(rnd == 1):
                gen = 1

        for gen in individual.Chromatine2:
            rnd = random.randint(1, 33) #3% na mutację
            if(rnd == 1):
                gen = 1;
        return individual

    def __CrosingOver(self, individual):
        rnd_crossingOver = random.randint(1, 33)
        if(rnd_crossingOver == 1):
            rnd_loci = random.randint(0, len(individual.Chromatine1))
            while(rnd_loci > len(individual.Chromatine1)):
                memory_gen = individual.Chromatine1[rnd_loci]
                individual.Chromatine1[rnd_loci] = individual.Chromatine2[rnd_loci]
                individual.Chromatine2[rnd_loci] = memory_gen

                rnd_loci += 1

        return individual

    def __Replicate(self, gametes_father, gametes_mother):
        newborn = Individual()
        rnd = random.randint(0, 1)
        newborn.Chromatine1 = gametes_father
        rnd = random.randint(0, 1)
        newborn.Chromatine2 = gametes_mother
        newborn.Sex = random.randint(0, 1)
        newborn.ProcreationAge = 16
        newborn.Age = 1
        newborn.T = 0
        newborn.Genotype.append(newborn.Chromatine1)
        newborn.Genotype.append(newborn.Chromatine2)
        return newborn

    def __GametesCreation(self, individual):
        gametes = []
        gamet1 = individual.Chromatine1
        gamet2 = individual.Chromatine2
        gametes.append(gamet1)
        gametes.append(gamet2)
        return gametes
