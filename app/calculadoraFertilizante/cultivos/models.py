from django.db import models

# Modelo para almacenar tipos de cultivo
class TipoCultivo(models.Model):
    nombre = models.CharField(max_length=50)  # Campo para el nombre del tipo de cultivo

    def __str__(self):
        return self.nombre  # Devuelve el nombre del tipo de cultivo como representación de cadena

# Modelo para almacenar información sobre los cultivos y sus componentes químicos
class Cultivo(models.Model):
    nombre = models.CharField(max_length=50)  # Campo para el nombre del cultivo
    tipo_cultivo = models.ForeignKey("cultivos.TipoCultivo", verbose_name="Tipo Cultivo", on_delete=models.CASCADE)  # Relación Muchos a Uno con TipoCultivo
    # Campos para los componentes químicos y sus índices de criticidad
    N = models.FloatField(default=0.0)
    P = models.FloatField(default=0.0)
    K = models.FloatField(default=0.0)
    Ca = models.FloatField(default=0.0)
    Mg = models.FloatField(default=0.0)
    S = models.FloatField(default=0.0)
    B = models.FloatField(default=0.0)
    Cl = models.FloatField(default=0.0)
    Cu = models.FloatField(default=0.0)
    Fe = models.FloatField(default=0.0)
    Mn = models.FloatField(default=0.0)
    Mo = models.FloatField(default=0.0)
    Zn = models.FloatField(default=0.0)
    Ni = models.FloatField(default=0.0)
    # Campos para los índices de criticidad de cada componente químico
    icN = models.FloatField(default=0.0)
    icP = models.FloatField(default=0.0)
    icK = models.FloatField(default=0.0)
    icCa = models.FloatField(default=0.0)
    icMg = models.FloatField(default=0.0)
    icS = models.FloatField(default=0.0)
    icB = models.FloatField(default=0.0)
    icCl = models.FloatField(default=0.0)
    icCu = models.FloatField(default=0.0)
    icFe = models.FloatField(default=0.0)
    icMn = models.FloatField(default=0.0)
    icMo = models.FloatField(default=0.0)
    icZn = models.FloatField(default=0.0)
    icNi = models.FloatField(default=0.0)

    # Método para obtener una representación legible del objeto Cultivo
    def str(self):
        nutrientes = {
            "N": self.N, "P": self.P, "K": self.K, "Ca": self.Ca, "Mg": self.Mg,
            "S": self.S, "B": self.B, "Cl": self.Cl, "Cu": self.Cu, "Fe": self.Fe,
            "Mn": self.Mn, "Mo": self.Mo, "Zn": self.Zn, "Ni": self.Ni
        }
        ics = {
            "icN": self.icN, "icP": self.icP, "icK": self.icK, "icCa": self.icCa,
            "icMg": self.icMg, "icS": self.icS, "icB": self.icB, "icCl": self.icCl,
            "icCu": self.icCu, "icFe": self.icFe, "icMn": self.icMn, "icMo": self.icMo,
            "icZn": self.icZn, "icNi": self.icNi
        }
        return self.nombre, self.tipo_cultivo, nutrientes, ics
