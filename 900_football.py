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


def main():
    p = input()
    print("YES" if "1111111" in p or "0000000" in p else "NO")


if __name__ == "__main__":
    main()
