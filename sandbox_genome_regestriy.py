from sandbox_genome import SandboxGenome

class GenomeRegistry:

    def __init__(self):
        self.genomes = {}

    def register(self, box):
        self.genomes[box] = SandboxGenome(box)

    def evolve(self, metrics):
        for g in self.genomes.values():
            g.fitness(metrics)
            g.mutate()