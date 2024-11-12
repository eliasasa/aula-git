class Animal:
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo):
        self.nomec = nomec                
        self.nome_cientifico = nome_cientifico  
        self.som = som                    
        self.alimentacao = alimentacao    
        self.membros = membros             
        self.filo = filo                  

    def emitir_som(self):
        if self.som:
            return f"{self.nomec} faz: {self.som}."
        else: return f"{self.nomec} não faz som."

    def info(self):
        return (f"Nome Comum: {self.nomec}, "
                f"Nome Científico: {self.nome_cientifico}, "
                f"Alimentação: {self.alimentacao}, "
                f"Membros: {self.membros}, "
                f"Filo: {self.filo}")


class Vertebrado(Animal):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.coluna_vertebral = True


class Mamifero(Vertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_pelo, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_pelo = tipo_pelo              
        self.habitat = habitat                  

    def pelos(self):
        return f"O mamífero {self.nomec} possui pelos!"


class Ave(Vertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_pena, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_pena = tipo_pena              
        self.habitat = habitat                  

    def penas(self):
        return f"A ave {self.nomec} possui penas do tipo: {self.tipo_pena}."


class Reptil(Vertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_escamas, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_escamas = tipo_escamas        
        self.habitat = habitat                  

    def escamas(self):
        return f"O réptil {self.nomec} possui escamas do tipo: {self.tipo_escamas}."


class Anfibio(Vertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_pele, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_pele = tipo_pele              
        self.habitat = habitat                  

    def pele(self):
        return f"O anfíbio {self.nomec} possui pele do tipo: {self.tipo_pele}."


class Invertebrado(Animal):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.coluna_vertebral = False


class Artrópode(Invertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_exoesqueleto, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_exoesqueleto = tipo_exoesqueleto  
        self.habitat = habitat                  

    def exoesqueleto(self):
        return f"O artrópode {self.nomec} possui um exoesqueleto do tipo: {self.tipo_exoesqueleto}."


class Molusco(Invertebrado):
    def __init__(self, nomec, nome_cientifico, som, alimentacao, membros, filo, tipo_concha, habitat):
        super().__init__(nomec, nome_cientifico, som, alimentacao, membros, filo)
        self.tipo_concha = tipo_concha          
        self.habitat = habitat                  

    def concha(self):
        return f"O molusco {self.nomec} possui uma concha do tipo: {self.tipo_concha}."

leão = Mamifero("Leão", "Panthera leo", "Rugido", "Carnívoro", 4, "Chordata", "Curto e denso", "Savana")
print(leão.info())
print(leão.emitir_som())
print(leão.pelos())

papagaio = Ave("Papagaio", "Amazona aestiva", "Parlar", "Herbívoro", 2, "Chordata", "Colorida", "Floresta")
print(papagaio.info())
print(papagaio.emitir_som())
print(papagaio.penas())

cobra = Reptil("Cobra", "Serpentes", "Sibilar", "Carnívoro", 0, "Chordata", "Lisa", "Deserto")
print(cobra.info())
print(cobra.emitir_som())
print(cobra.escamas())

sapo = Anfibio("Sapo", "Bufo bufo", "Coaxar", "Onívoro", 4, "Chordata", "Húmida", "Pântano")
print(sapo.info())
print(sapo.emitir_som())
print(sapo.pele())

# Invertebrados
aranha = Artrópode("Aranha", "Araneae", False, "Carnívoro", 8, "Arthropoda", "Quitinoso", "Floresta")
print(aranha.info())
print(aranha.emitir_som())
print(aranha.exoesqueleto())

caramujo = Molusco("Caramujo", "Helix aspersa", False, "Herbívoro", 0, "Mollusca", "Espiral", "Jardim")
print(caramujo.info())
print(caramujo.emitir_som())
print(caramujo.concha())
