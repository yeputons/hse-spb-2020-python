#!/usr/bin/env python3
# Comma-Separated Values
import csv

with open("data.csv") as f:
    for row in csv.DictReader(f):
        print(row)

# JSON
# YAML
