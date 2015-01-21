#!/usr/bin/env python

import csv
import json
import os
import sys


def format_entities_as_list(entities):
    for i, entity in enumerate(entities, 1):
        yield (unicode(i), json.dumps(entity["terms"]))


def generate_entities(fobj):
    termsets_seen = set()
    for line in fobj:
        entity = json.loads(line)
        termset = tuple(entity["terms"])
        if termset not in termsets_seen:
            termsets_seen.add(termset)
            yield entity


def load_entities_from_file(infile, outfile):
    if os.path.exists(outfile):
        raise RuntimeError("Output file %r already exists" % outfile)
    with open(infile) as in_fobj:
        with open(outfile, "wb") as out_fobj:
            writer = csv.writer(out_fobj)
            for row in format_entities_as_list(generate_entities(in_fobj)):
                writer.writerow(row)


if __name__ == '__main__':
    load_entities_from_file(sys.argv[1], sys.argv[2])
