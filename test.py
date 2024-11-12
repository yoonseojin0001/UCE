import argparse

parser = argparse.ArgumentParser(description="A simple argument parser example")

parser.add_argument("--name", required=False, help="Your name")
parser.add_argument("--age", required=True, type=int, help="Your age")

args = parser.parse_args()

# 인자 출력
print("Name:", args.name)
print("Age:", args.age)