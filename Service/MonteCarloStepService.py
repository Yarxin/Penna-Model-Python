from Factory.IndividualFactory import IndividualFactory
from Service.GeneticOperationService import GeneticOperationService
import random

class MonteCarloStepService:

# Kolejne kroki:
# 1.Podział populacji na samców i samice
# 2.Sprawdzanie wieku z parametrem
# 3.Rozmnóż
# 4.Zabij osobniki, jeśli pojemność środowiska zostaje przekroczona.

    def MonteCarloStep(self, population, param_R, param_T):
        self.__CalculateGeneticAge(population, param_T)
        procreation_population = self.__CheckGeneticAge(population, param_R)
        split_population = self.__SplitPopulation(procreation_population)
        population = self.__Procreate(split_population, population)

    def __CalculateGeneticAge(self, population, param_T): #określ wiek na podstawie kroku MonteCarlo
        for individual in population:
            individual.Age += 1
            deleted_individ = False
            for loci, index in enumerate(individual.Chromatine1):
                if(loci == 1 and individual.Chromatine2[index] == 1):
                    individual.T += 1
                    if individual.T >= param_T:
                        print("Z powodów genetycznych umarł osobnik w wieku: " + str(individual.Age))
                        population.remove(individual) #pora umierać.
                        deleted_individ = True

            time_to_die = random.randint(0, 5)
            if individual.Age >= 80 and deleted_individ == False:
                if time_to_die == 1:
                    population.remove(individual)
                    print("RIP ze starości osobnik w wieku: " + str(individual.Age))

    def __CheckGeneticAge(self, population, param_R): #znajdź osobniki w wieku pozwalającym na rozród
        procreation_population = []
        for individ in population:
            if individ.Age >= param_R:
                procreation_population.append(individ)
        return procreation_population

    def __SplitPopulation(self, population): #podziel populacę na samice i samców
        split_population = []
        male_list = []
        female_list = []
        for individ in population:
            if individ.Sex == 0:
                female_list.append(individ)
            else:
                male_list.append(individ)
        split_population.append(male_list)
        split_population.append(female_list)
        return split_population

    def __Procreate(self, split_population, population):
        genOps = GeneticOperationService()
        for femindivid in split_population[0]:
            genOps.MutateIndividual(femindivid)
            genOps.CrossingOverIndividual(femindivid)
            genOps.GametesCreationIndividual(femindivid)
        for menindivid in split_population[1]:
            genOps.MutateIndividual(menindivid)
            genOps.CrossingOverIndividual(menindivid)
            genOps.GametesCreationIndividual(menindivid)
        i = 0
        for femindivid in split_population[0]:
            if i < len(split_population[1]):
                procreate = random.randint(1, 33)
                if procreate == 1:
                    newborn = genOps.ReplicateIndividual(femindivid.Chromatine1, split_population[1][i].Chromatine2)
                    population.append(newborn)
                i += 1
            else:
                break
        return population



