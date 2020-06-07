def es_ano_bisiesto(ano):
    if ano % 4 == 0 or (ano % 100 == 0 and ano % 400 != 0):
        return True
    else:
        return False


def fecha_valida(dia, mes, ano):
    meses_con_30_dias = (4, 6, 9, 11)
    meses_con_31_dias = (1, 3, 5, 7, 8, 10, 12)

    if mes in meses_con_30_dias:
        if dia <= 30:
            return True
        else:
            return False
    elif mes in meses_con_31_dias:
        if dia <= 31:
            return True
        else:
            return False
    if mes == 2:
        if es_ano_bisiesto(ano):
            if dia <= 29:
                return True
            else:
                return False
        else:
            if dia <= 28:
                return True
            else:
                return False


class Fecha:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.dia, self.mes, self.ano)

    def agregar_dias(self, dias):
        meses_con_30_dias = (4, 6, 9, 11)
        meses_con_31_dias = (1, 3, 5, 7, 8, 10)
        dia, mes, ano = self.dia+dias, self.mes, self.ano

        if self.mes in meses_con_30_dias:
            if dia > 30:
                mes += 1
                dia = dia-30

        elif self.mes in meses_con_31_dias:
            if dia > 31:
                mes += 1
                dia = dia-31

        if self.mes == 2:
            if es_ano_bisiesto(self.ano):
                if dia > 29:
                    mes += 1
                    dia = dia-29
            else:
                if dia > 28:
                    mes += 1
                    dia = dia-28
        if self.mes == 12:
            if dia > 31:
                ano += 1
                mes = 1
                dia = dia-31

        return Fecha(dia, mes, ano)
