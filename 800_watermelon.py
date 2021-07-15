#: GENERATED USING: `python3 -m file_generator Watermelon 800 4A`
#:
#: Name: Watermelon
#: Diffculity: 800
#: Problem source: https://codeforces.com/problemset/problem/4/A
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

print_no = lambda: print("NO")
print_yes = lambda: print("YES")
is_even = lambda x: x % 2 == 0


def main():
    w = int(input())
    if not is_even(w):
        print_no()
        return

    part1 = part2 = w / 2
    while part1 > 0 and part2 > 0:
        if is_even(part1) and is_even(part2):
            print_yes()
            break
        part1 += 1
        part2 -= 1
    else:
        print_no()


if __name__ == "__main__":
    main()
