__author__ = 'kumar_garg'

import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        """ Adds two vector
        :param v: vector to be added to the current vector
        :return: new vector which represents the addition of two vectors
        """
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def minus(self, v):
        """ Subtract vector by input argument from the current vector
        :param v: vector to be subtracted from the current vector
        :return: new vector which represent the subtraction of two vectors
        """
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def scaleVector(self, scalar):
        """ Scale vector by the given scalar

        :param scalar: amount by which input vector needs to be scaled
        :return: scaled vector
        """
        return Vector([Decimal(scalar) * x for x in self.coordinates])

    def magnitude(self):
        """ Calculates the magnitude of vector"""
        l = sum([x ** 2 for x in self.coordinates])
        return Decimal(math.sqrt(l))

    def unitVector(self):
        """ Return unit vector """
        m = self.magnitude()
        if not m:
            return None
        return self.scaleVector(Decimal('1.0') / m)

    def dotProduct(self, v):
        """ Calculates dot product between two vectors
        :param v: vector with which dot product needs to be calculated
        :return: dot product
        """
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degrees=False):
        x = self.unitVector()
        y = v.unitVector()

        if x is None or y is None:
            return None

        if in_degrees:
            return Decimal(math.acos(x.dotProduct(y))) * Decimal(180.) / Decimal(math.pi)
        else:
            return Decimal(math.acos(round(x.dotProduct(y), 3)))

    def isParallel(self, v):
        """ Checks if two vectors are parallel
        :param v: input vector
        :param tolerance: to account for floating point arithmetic
        :return: true if current vector parallel to input vector, false otherwise
        """
        return (self.is_zero() or
                v.is_zero() or
                self.angle(v) == 0 or
                self.angle(v) == math.pi)

    def is_zero(self, tolerance=1e-10):
        """ Returns true if current vector is zero
        """
        return self.magnitude() < tolerance

    def isOrthogonal(self, v, tolerance=1e-10):
        """ Checks if two vectors are orthogonal

        :param v: input vector
        :param tolerance: to account for floating point arithmetic
        :return: true if current vector parallel to input vector, false otherwise
        """
        if math.fabs(self.dotProduct(v)) <= tolerance:
            return True
        return False

    def projection(self, b):
        """ Captures projection of current vector on vector b

        :param b: input vector
        :return: Projection Vector
        """
        u = b.unitVector()
        return u.scaleVector(self.dotProduct(u))


vector1 = Vector([3.039, 1.879])
vector2 = Vector([0.825, 2.036])
print vector1.projection(vector2)

vector3 = Vector([-9.88, -3.264, -8.159])
vector4 = Vector([-2.155, -9.353, -9.473])
p = vector3.projection(vector4)
print vector3.minus(p)

vector5 = Vector([3.009, -6.172, 3.692, -2.51])
vector6 = Vector([6.404, -9.144, 2.759, 8.718])
p = vector5.projection(vector6)
print p
print vector5.minus(p)
