class CalculatorClass:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
        return x / y

# ------------------------------
# Test
# ------------------------------
calc = CalculatorClass()
print "5 + 3 = ", calc.add(5, 3)
print "5 - 3 = ", calc.sub(5, 3)
print "5 * 3 = ", calc.mul(5, 3)
print "5 / 3 = ", calc.div(5, 3)