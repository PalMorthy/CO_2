from typing import Union, List
import math
import doctest

# TODO Написать 3 класса с документацией и аннотацией типов


class Point2D:
    def __init__(self, x: Union[float, int], y: Union[float, int]):
        """
        Creates a 2D point with X, Y coordinates
        :param x: point x-coordinate
        :param y: point y-coordinate
        Examples:
        >>> point = Point2D(10, 1)
        """
        """
        TEST UNIT:
        ~~~~~~~~~~
            Here the input parameters are checked
        """
        if not isinstance(x, (int, float)):
            raise TypeError(f"x - {x} must be int or float")

        if not isinstance(y, (int, float)):
            raise TypeError(f"y - {y} must be int or float")

        self.X = x
        self.Y = y

    def create_point(self) -> tuple:
        """
        Create a list containing a point.
        :return: List [X, Y]
        Examples:
        >>> point = Point2D(1, 2)
        >>> point.create_point() == (1, 2)
        True
        """

        out_point = (self.X, self.Y)
        return out_point

    def mult_point_by_num(self, a_x: Union[float, int, complex], b_y: Union[float, int, complex]) -> tuple:
        """
        Multiplies the x and y coordinates of a point by two numbers
        :param a_x: The number by which the X coordinate is multiplied
        :param b_y: The number by which the Y coordinate is multiplied
        :return: List [X * a_x, Y * b_y]
         Examples:
        >>> point = Point2D(1, 2)
        >>> point.mult_point_by_num(2, 2) == (2, 4)
        True
        """
        if not isinstance(a_x, (int, float, complex)):
            raise TypeError(f"x - {a_x} must be int or float")

        if not isinstance(b_y, (int, float, complex)):
            raise TypeError(f"y - {b_y} must be int or float")

        out_mult_point = (self.X * a_x, self.Y * b_y)
        return out_mult_point


class Vector2D:

    def __init__(self, first_point: Point2D, second_point: Point2D):
        """
        Creates a 2D row vector
        :param first_point: Vector Startpoint
        :param second_point: Vector Endpoint
        Exmples:
        >>> vector = Vector2D(Point2D(1, 1), Point2D(2,2))
        >>> vector.vector == [2 - 1, 2 - 1]
        True
        """
        if not isinstance(first_point, Point2D):
            raise TypeError(f"first point - {first_point} must be Point2D")

        if not isinstance(second_point, Point2D):
            raise TypeError(f"second point - {second_point} must be Point2D")
        self.first_pointX, self.first_pointY = first_point.create_point()[0], first_point.create_point()[1]
        self.second_pointX, self.second_pointY = second_point.create_point()[0], second_point.create_point()[1]
        self.vector = [self.second_pointX - self.first_pointX, self.second_pointY - self.first_pointY]

    def vector_2dim_len(self) -> float:
        """
        The length of the vector is calculated
        :return: The length of the vector
        Examples:
        >>> vector = Vector2D(Point2D(2, 2), Point2D(3, 3))
        >>> vector.vector_2dim_len() == math.sqrt(2)
        True
        """
        out_len = math.sqrt(self.vector[0] ** 2 + self.vector[1] ** 2)
        return out_len

    def mult_vect_by_num(self, num: Union[float, int]) -> List:
        """
        Multiplies a vector by a number
        :param num: The multiplied number
        :return: The new vector
        Examples:
        >>> vector = Vector2D(Point2D(1, 1), Point2D(3, 2))
        >>> vector.mult_vect_by_num(2) == [4, 2]
        True
        """
        if not isinstance(num, (int, float)):
            raise TypeError(f"num - {num} must be int or float")

        out_vector = [self.vector[0] * num, self.vector[1] * num]
        return out_vector

    def add_num_to_vector(self, num: Union[int, float]) -> List:
        """
        Adds a number to a vector
        :param num: The added number
        :return: The new vector
        Examples:
        >>> vector = Vector2D(Point2D(1, 1), Point2D(2, 2))
        >>> vector.add_num_to_vector(2) == [3, 3]
        True
        """
        if not isinstance(num, (int, float)):
            raise TypeError(f"num - {num} must be int or float")

        out_vector = [self.vector[0] + num, self.vector[1] + num]
        return out_vector


class Matrix2D:
    def __init__(self, first_vector: Vector2D, second_vector: Vector2D):
        """
        Creates a two-dimensional array
        :param first_vector: First column of the matrix
        :param second_vector: Second column of the matrix
        Examples:
        >>> point1, point2, point3, point4 = Point2D(1, 1), Point2D(2, 2), Point2D(2, 2), Point2D(4, 4)
        >>> vector1, vector2 = Vector2D(point1, point2), Vector2D(point3, point4)
        >>> matrix = Matrix2D(vector1, vector2)
        >>> matrix.matrices == [[1, 1], [2, 2]]
        True
        """
        if not isinstance(first_vector, Vector2D):
            raise TypeError(f"first point - {first_vector} must be Vector2D")

        if not isinstance(second_vector, Vector2D):
            raise TypeError(f"second point - {second_vector} must be Vector2D")

        self.matrices = [first_vector.vector, second_vector.vector]

    def calculate_det(self) -> Union[float, int]:
        """
        Calculates The determinant of a matrix
        :return: The determinant of a matrix
        Examples:
        >>> point1, point2, point3, point4 = Point2D(1, 1), Point2D(2, 2), Point2D(2, 2), Point2D(4, 4)
        >>> vector1, vector2 = Vector2D(point1, point2), Vector2D(point3, point4)
        >>> matrix = Matrix2D(vector1, vector2)
        >>> matrix.calculate_det()
        """
        ...

    def add_num_to_matrices(self, num: Union[float, int]) -> List:
        """
        Adds a number to all elements of a matrix
        :return: The new Matrix
        :param num: The added number
        Examples:
        >>> point1, point2, point3, point4 = Point2D(1, 1), Point2D(2, 2), Point2D(2, 2), Point2D(4, 4)
        >>> vector1, vector2 = Vector2D(point1, point2), Vector2D(point3, point4)
        >>> matrix = Matrix2D(vector1, vector2)
        >>> matrix.add_num_to_matrices(2.2)
        """
        ...

    def mult_matrices_by_num(self, num: Union[float, int]) -> List:
        """
        Adds a number to all elements of a matrix
        :return: The new Matrix
        :param num: The multiplied number
        Examples:
        >>> point1, point2, point3, point4 = Point2D(1, 1), Point2D(2, 2), Point2D(2, 2), Point2D(4, 4)
        >>> vector1, vector2 = Vector2D(point1, point2), Vector2D(point3, point4)
        >>> matrix = Matrix2D(vector1, vector2)
        >>> matrix.mult_matrices_by_num(2)
        """
        if not isinstance(num, (int, float)):
            raise TypeError(f"num - {num} must be int or float")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
