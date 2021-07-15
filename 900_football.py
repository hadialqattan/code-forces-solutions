#: GENERATED USING: `python3 -m file_generator Football 900 96A`
#:
#: Name: Football
#: Diffculity: 900
#: Problem source: https://codeforces.com/problemset/problem/96/A
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


def main():
    positions = input()
    same_team_counter = 0
    prev_position = positions[0]
    for p in positions:

        if p == prev_position:
            # add two if `same_team_counter` equals zero.
            same_team_counter += 1 if same_team_counter else 2
        else:
            same_team_counter = 0

        if same_team_counter == 7:
            print_yes()
            break

        prev_position = p
    else:
        print_no()


if __name__ == "__main__":
    main()
