import sys

from day1.Solver import Solver

def main(day: str, input_file) -> None:
    mod = __import__("day" + day + ".Solver", fromlist=['Solver'])
    solver_class = getattr(mod, 'Solver')

    solver = solver_class("data/day"+day+"/"+input_file)

    solver.execute()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
