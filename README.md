
# Interview practice

I'm going to be interviewing shortly, so I'm getting back into practice with this type
of problem solving

# Disabling auto formatting and linting

I use autopep8, pylint on vscode typically. I've turned that off here for now - I'm using
Python 3.8, and those formatting changes haven't propagated through to my linting stack
fully, so I just turned it off for this small project. Almost certainly this'll propagate
through in due time, all of those are still maintained.

This does mean my code will be linted by eye, so it likely won't be as good

(I really want that walrus)

# To revisit

These I found hard
- geeksforgeeks/graph/bfs
- geeksforgeeks/graph/detect_cycle/naive

## hackerrank/data_structures/trie/contacts.py

I did a full implementation of a trie, but really the question didn't need the the prefix completion, just to know the number of nodes in the subtree, which was easy to store at insert time.

It also wasn't fast enough with the initial recursive solution I tried, but an (arguably simpler) iterative solution with the add was fast enough.

## hackerrank/sql/*

New concepts
- multiple ORDER BY
- LEFT, RIGHT, SUBSTRING, REGEXP
- IF, CASE WHEN
- EXISTS
- COUNT (without GROUP BY)
