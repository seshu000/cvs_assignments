from itertools import zip_longest

class Poly:
    def __init__(self, *coef):
        self.coef = list(coef)
        
    def __str__(self):
        coef_str = ', '.join(str(c) for c in self.coef)
        return "Poly(" + coef_str + ")"

    def __add__(self, other):
        result_coef = [
            a + b for a, b in zip_longest(self.coef[::-1], other.coef[::-1], fillvalue=0)
        ][::-1]
        return Poly(*list(result_coef))






