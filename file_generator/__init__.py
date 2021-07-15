"""Solution file generator"""
from datetime import datetime
import argparse

FILE_TEMPLATE = """#: GENERATED USING: `python3 -m file_generator {real_name} {diffculity} {real_id}`
#:
#: Name: {parsed_name}
#: Diffculity: {diffculity}
#: Problem source: https://codeforces.com/problemset/problem/{parsed_id}
#: 
#: MIT License
#:
#: Copyright (c) {year} Hadi Alqattan <alqattanhadizaki@gmail.com>
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
#: My solution <{date}>:


def main():
    pass


if __name__ == "__main__":
    main()
"""


def argsp() -> list:
    parser = argparse.ArgumentParser(
        prog="SFGenerator",
        description="Solution file generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "name", type=str, nargs=1, help="problem title/name, e.g Potato"
    )
    parser.add_argument(
        "diffculity", type=int, nargs=1, help="problem diffculity, e.g 800"
    )
    parser.add_argument("id", type=str, nargs=1, help="problem id, e.g 96A")
    args = parser.parse_args()

    def _id_parser(_id: str) -> str:
        for i, c in enumerate(_id):
            if not c.isdigit():
                return _id[:i] + "/" + _id[i:]
        assert False, f"Invalid problem Id: {_id}"

    args.id = _id_parser(args.id[0])
    args.diffculity = str(args.diffculity[0])
    args.name = args.name[0]
    return args


def main():
    args = argsp()
    file_name = args.diffculity + "_" + args.name.lower() + ".py"
    with open(file_name, "w+") as f:
        this_year = datetime.now().year
        f.write(
            FILE_TEMPLATE.format(
                real_name=args.name,
                parsed_name=args.name.replace("_", " "),
                diffculity=args.diffculity,
                real_id=args.id.replace("/", ""),
                parsed_id=args.id,
                year=this_year,
                date=datetime.now().strftime("%Y-%m-%d"),
            )
        )


if __name__ == "__main__":
    main()
