# Комплексные числа.

import sys


class ComplexNumber(object):
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __mul__(self, other):
        new_real = self.real * other.real - \
            self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + \
            self.imaginary * other.real
        return ComplexNumber(new_real, new_imaginary)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __truediv__(self, other):
        abs_value = other.real ** 2 + other.imaginary ** 2
        new_real = (
            self.real * other.real +
            self.imaginary * other.imaginary) / abs_value
        new_imaginary = (
            self.imaginary * other.real -
            self.real * other.imaginary) / abs_value
        return ComplexNumber(new_real, new_imaginary)

    def __str__(self):
        if self.real == 0:
            if self.imaginary == 0:
                return str("%.2f" % 0.00)
            return str("%.2f" % self.imaginary) + "i"
        if self.imaginary == 0:
            return str("%.2f" % self.real)
        if self.imaginary > 0:
            return str("%.2f" % self.real) + " + " + \
                   str("%.2f" % self.imaginary) + "i"
        if self.imaginary < 0:
            return str("%.2f" % self.real) + " - " + \
                   str("%.2f" % -self.imaginary) + "i"

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
