from Factory.IndividualFactory import IndividualFactory
from Service.MonteCarloStepService import MonteCarloStepService
from matplotlib import pyplot as plt

########################## Sekcja Interaktywna ##########################
# print("Minimalną liczbę fenotypowych defektów powodujących śmierć genetyczną")
# T = int(input())
#
# print("Podaj liczebność populacji")
# number_of_individs = int(input())
#
# print("Podaj liczbę genów pojedyńczego osobnika")
# number_of_genes = int(input())
#
# print("Podaj wiek prokreacji osobników")
# procreation_age = int(input())

### Sex -> 0 == female, 1 == male ###

T = 40 #min number of fenotype defects, couses death
number_of_individs = 10
number_of_genes = 100
procreation_age = 16 #param_R
maxPopulation = 15

#########################################################################


########################## Sekcja Symulacyjna ##########################
individualFactory = IndividualFactory()

population = individualFactory.CreatePopuation(number_of_genes, number_of_individs, T, procreation_age)
monteCarloStepService = MonteCarloStepService()
i = 0
defectiveGenesList = []
while i < number_of_genes:
    defectiveGenesCount = 0
    monteCarloStepService.MonteCarloStep(population, procreation_age, T)
    for individ in population:
        j = 0
        for gene in individ.Chromatine1:
            if gene == 1 and individ.Chromatine2[j] == 1:
                defectiveGenesCount += 1
                j += 1
            else:
                j += 1
    defectiveGenesList.append(defectiveGenesCount)
    environmental_capacity = 1 - (len(population) / maxPopulation)
    if environmental_capacity == 0:
        while environmental_capacity <= 0:
            population.remove(population[0])
            environmental_capacity = 1 - (len(population) / maxPopulation)
    i += 1
    print(str(i))

years = []
i = 1
for gene in defectiveGenesList:
    years.append(i)
    i += 1

plt.plot(years, defectiveGenesList, '.')
plt.ylabel("liczba defektywnych genów")
plt.xlabel("wiek")
plt.grid(color='black')
plt.show()
