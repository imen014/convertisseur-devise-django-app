class Convertisseur:
    def __init__(self, amount_to_convert, initial_unitee, unitee_of_conversion):
        self.amount_to_convert = amount_to_convert
        self.initial_unitee = initial_unitee
        self.unitee_of_conversion = unitee_of_conversion

    def convertir_devise(self):
        if self.initial_unitee == "dollar" and self.unitee_of_conversion == "dinars":
            self.result_amount = self.amount_to_convert * 3.3
        elif self.initial_unitee == "dinars" and self.unitee_of_conversion == "dollar":
            self.result_amount = self.amount_to_convert / 3.3
        elif self.initial_unitee == "dinars" and self.unitee_of_conversion == "euros":
            self.result_amount = self.amount_to_convert / 3.5
        elif self.initial_unitee == "euros" and self.unitee_of_conversion == "dinars":
            self.result_amount = self.amount_to_convert * 3.5
        elif self.initial_unitee == "dollar" and self.unitee_of_conversion == "euros":
            self.result_amount = self.amount_to_convert * 1.25
        elif self.initial_unitee == "euros" and self.unitee_of_conversion == "dollar":
            self.result_amount = self.amount_to_convert / 1.25
        return self.result_amount
