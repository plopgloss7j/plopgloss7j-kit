"""Summarize numeric columns of a CSV file."""
from __future__ import annotations

import csv
from pathlib import Path

VERSION = "0.6.3"


class Plopgloss7jTool:
    """Mean / min / max per numeric column."""

    def summarize(self, path, column=None):
        target = Path(path)
        if not target.is_file():
            return {}
        with target.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            return {}
        fields = [column] if column else list(rows[0].keys())
        out = {}
        for field in fields:
            values = []
            for row in rows:
                try:
                    values.append(float(row.get(field, "")))
                except (TypeError, ValueError):
                    continue
            if values:
                out[field] = {"n": len(values), "min": min(values),
                              "max": max(values),
                              "mean": round(sum(values) / len(values), 4)}
        return out
