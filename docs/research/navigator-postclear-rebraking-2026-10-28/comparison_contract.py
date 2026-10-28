import os
from pathlib import Path
"""Fail-closed route coverage contract for replay comparisons."""

def matching_routes(bases, candidates, expected):

    def index(rows):
        if not rows:
            raise ValueError('Empty replay route corpus')
        names = [row['drive'] for row in rows]
        if len(names) != len(set(names)):
            raise ValueError('Duplicate replay route')
        return {row['drive']: row for row in rows}
    base, candidate, required = (index(bases), index(candidates), index(expected))
    if set(base) != set(required) or set(candidate) != set(required):
        raise ValueError('Missing or extra replay routes relative to input manifest')
    return candidate
