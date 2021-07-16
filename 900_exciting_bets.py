#: GENERATED USING: `python3 -m file_generator Exciting_Bets 900 1543A`
#:
#: Name: Exciting Bets
#: Diffculity: 900
#: Problem source: https://codeforces.com/problemset/problem/1543/A
#:
#: MIT License
#:
#: Copyright (c) 2021 Hadi Alqattan <alqattanhadizaki@gmail.com>
#:
#: Permission is hereby granted, free of charge, to any person obtaining a copy
#: of this software and associated documentation files (the "Software"), to deal
#: in the Software without restriction, including without limitation the rights
#: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#: copies of the Software, and to permit persons to whom the Software is
#: furnished to do so, subject to the following conditions:
#:
#: The above copyright notice and this permission notice shall be included in all
#: copies or substantial portions of the Software.
#:
#: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#: SOFTWARE.
#:
#: My solution <2021-07-16>:

output = lambda max_excitements, min_moves: print(max_excitements, min_moves)


def main():
    tests_count = int(input())
    for _ in range(tests_count):
        a, b = map(int, input().split())

        if a == b:
            output(0, 0)
            continue

        greatest_gcd = abs(a - b)
        minimum_moves = min(a % greatest_gcd, greatest_gcd - a % greatest_gcd)
        output(greatest_gcd, minimum_moves)


if __name__ == "__main__":
    main()
