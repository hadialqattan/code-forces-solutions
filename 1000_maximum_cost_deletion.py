#: GENERATED USING: `python3 -m file_generator Maximum_Cost_Deletion 1000 1550B`
#:
#: Name: Maximum Cost Deletion
#: Diffculity: 1000
#: Problem source: https://codeforces.com/problemset/problem/1550/B
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


def blocks_count(s: str) -> int:
    prev_i = None
    blocks = -1 if s[0] == s[-1] else 0
    for i in s:

        if prev_i is None:
            prev_i = i
            blocks += 1
            continue

        if prev_i != i:
            blocks += 1
        prev_i = i

    return blocks


def main():
    t = int(input())
    for _ in range(t):

        n, a, b = map(int, input().split())
        m = blocks_count(input())

        print(int(n * a + max(n * b, (m / 2 + 1) * b)))


if __name__ == "__main__":
    main()
