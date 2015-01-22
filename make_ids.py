#!/usr/bin/env python

import csv
import json
import os
import sys


def format_entities_as_list(entities):
    """Format entities read from an iterator as lists.

    :param entities: An iterator yielding entities as dicts:
           eg {"terms": ["Fred"]}

    Yield a sequence of entites formatted as lists containing string values.
    Also allocates identifier numbers.  Sequences are formatted as json.  eg:

        ["1", '["Fred"]']

    The resulting sequence is ideal for conversion to CSV.

    """
    for i, entity in enumerate(entities, 1):
        yield (unicode(i), json.dumps(entity["terms"]))


def generate_entities(fobj):
    """Generate entities by reading from a file object.

    :param fobj: File object to read from.  Each line in the file should
    represent an entity.

    Yields a sequence of dicts representing entities, where the dicts will
    contain at the least a "terms" object.

    """
    termsets_seen = set()
    for line in fobj:
        entity = json.loads(line)
        termset = tuple(entity["terms"])
        if termset not in termsets_seen:
            termsets_seen.add(termset)
            yield entity


def convert_entities_from_file_to_csv(infile, outfile):
    """Convert entities from a file to CSV format.

    :param infile: The file name to read entities from.  Formatted as jsonlines
    (http://jsonlines.org/) - one line per entity.

    :param outfile: The file name to write entities to as CSV.

    """
    if os.path.exists(outfile):
        raise RuntimeError("Output file %r already exists" % outfile)
    with open(infile) as in_fobj:
        with open(outfile, "wb") as out_fobj:
            writer = csv.writer(out_fobj)
            for row in format_entities_as_list(generate_entities(in_fobj)):
                writer.writerow(row)


if __name__ == '__main__':
    convert_entities_from_file_to_csv(sys.argv[1], sys.argv[2])
