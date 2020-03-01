# coding=utf-8

CUVEE_WIDTH = 0.3


def abs(x):
    if x < 0:
        return -x
    else:
        return x


def f(x, y):
    return y - x ** 3 - 2 * x ** 2 + 1 + x


class Cuvee(object):
    def __init__(self, expression, x_scope, y_scope, points):
        self.expression = expression  # this could be an equation
        self.x_scope = x_scope
        self.y_scope = y_scope
        self.points = points

    def __arange(self, begin, to, points):
        lis = [begin]
        deta = (to - begin) / (points - 1)
        for i in range(points - 1):
            lis.append(lis[i] + deta)
        return lis

    def __equation(self, x, y):
        if isinstance(self.expression, str):
            if abs(eval(self.expression)) < CUVEE_WIDTH:
                return x, y
            else:
                return None
        else:
            if abs(self.expression(x, y)) < CUVEE_WIDTH:
                return x, y
            else:
                return None

    def draw_all(self):
        print("^")
        for i in range(self.points):
            print("|", "*" * self.points)
        print("-" * self.points, ">")

    def __compute(self):
        res = []
        for x in self.__arange(self.x_scope[0], self.x_scope[1], self.points):
            for y in self.__arange(self.y_scope[0], self.y_scope[1], self.points):
                if self.__equation(x, y):
                    res.append((x, y))
                else:
                    pass
        return res

    def draw(self):
        for y in self.__arange(self.y_scope[1], self.y_scope[0], self.points):  # 便于显示倒过来了
            for x in self.__arange(self.x_scope[0], self.x_scope[1], self.points):
                if self.__equation(x, y):
                    print("@", end="")
                else:
                    print(".", end="")
            print()
        return None

    def show(self):
        point_set = self.__compute()
        self.draw()


if __name__ == '__main__':
    c = Cuvee(f, (-10, 10), (-10, 10), points=100)
    c.show()


    def f2(x, y):
        res = (1 - x ** 2) ** 0.5 - y
        if isinstance(res, complex):
            return 404
        else:
            if y > 0:
                return res
            else:
                return -(1 - x ** 2) ** 0.5 - y
    # c = Cuvee(f2, (-5, 5), (-5, 5), points=50)
    # c.show()
