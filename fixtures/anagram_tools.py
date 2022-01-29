#!/bin/python3
import collections

def is_anagram(string_1: str, string_2: str) -> bool:
    return _get_count_representation(string_1.lower()) == _get_count_representation(string_2.lower())

def _get_count_representation(string: str) -> str:
    counter = collections.Counter(sorted(string))
    return "".join([f"{key}{count if count > 1 else ''}" for key, count in counter.items()])

def main():
    random_string = "bbaatest"
    print(f"Count representation of '{random_string}': {_get_count_representation('bbaatest')}")

    anagram_string_1 = "east"
    anagram_string_2 = "seat"
    print(f"'{anagram_string_1}', is an anagram of '{anagram_string_2}'? {is_anagram(anagram_string_1, anagram_string_2)}")

if __name__ == "__main__":
    main()
