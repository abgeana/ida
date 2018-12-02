#! env python3

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="generate ida struct definitions")
    parser.add_argument("--name", type=str, default="ag_type_t", help="name of the struct")
    parser.add_argument("--type", type=str, default="unsigned __int8", help="type of each struct member")
    parser.add_argument("--size", type=int, default=10, help="number of members for the struct")
    parser.add_argument("--start", type=int, default=0, help="start index for member names")
    parser.add_argument("--bare", action="store_true", help="print the bare members without the struct definition")
    return parser.parse_args()

def main():
    args = parse_args()
    definition = str()

    if not args.bare:
        definition += "struct {name} {{\n".format(name=args.name)

    for idx in range(args.size):
        definition += "    {type} var{idx};\n".format(type=args.type, idx=args.start + idx)

    if not args.bare:
        definition += "}}\n".format(name=args.name)

    print(definition)

if __name__ == "__main__":
    main()
