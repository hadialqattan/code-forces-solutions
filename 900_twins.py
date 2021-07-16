#: GENERATED USING: `python3 -m file_generator Twins 900 160A`
#:
#: Name: Twins
#: Diffculity: 900
#: Problem source: https://codeforces.com/problemset/problem/160/A
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


def main():
    _ = input()  # no need!
    values = sorted(map(int, input().split()), reverse=True)
    half_sum = sum(values) / 2
    my_sum = my_coins_counter = 0
    for value in values:
        my_sum += value
        my_coins_counter += 1
        if my_sum > half_sum:
            break
    print(my_coins_counter)


if __name__ == "__main__":
    main()
