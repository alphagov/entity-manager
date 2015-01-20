# Entity Manager

This takes lists of entities or suspected entities from many sources and
combines them to produce a set of entities in which we have sufficient
confidence to use them in search.  It also assigns persistent ids to each
entity.

## Nomenclature

- **Entity**: an entity is any well known real world thing such as a person,
  place, organisation, policy etc.  For example, "HM Revenue and Customs".

- **Term**: a string used to refer to the entity.  A single entity may be
  represented by multiple terms.  For example, "HMRC", "Revenue and Customs"
  would be terms for the "HM Revenue and Customs" entity.

## Technical documentation

This is currently a python script which is passed a set of files containing
entity information.  It scans through these files, attempting to map the
entities in them to entities in its database.  For entities which aren't found
in the database, a new entry and persistent identifier is allocated for the
entity.

## Dependencies

 - [Python](https://www.python.org/) - version 2.7.
 - [postgres](http://www.postgresql.org/) - stores entities and terms.
   Required to ensure that consistent IDs are applied.
 - [nltk](http://www.nltk.org/) - for text analysis.

## Running the application

Prepare a virtualenv and install packages with
```
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Then, run the script with
`./manage-entites.py [entity files]`

A file of currently known entities can be produced, in a form suitable for
loading into a Postgres database, by running:

`./dump-entites.py`

## Running the test suite

Assuming the virtualenv has been created, activated and packages have been
installed:

`./run-tests.sh`

## Licence

[MIT License](LICENCE)
