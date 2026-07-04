#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prompt Warrior — duel: compare two profile.json files (same scale version).

Usage:
  python compare.py mine.json theirs.json [--names "Я" "Друг"]
Prints a text versus card to the console.
"""
import argparse
import json
import sys


def bar(v, width=10):
    v = max(0, min(100, v or 0))
    full = int(round(v / 100 * width))
    return "█" * full + "░" * (width - full)


def main():
    ap = argparse.ArgumentParser(description="Duel of two Prompt Warrior profiles")
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--names", nargs=2, default=None)
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    pa = json.load(open(args.a, encoding="utf-8"))
    pb = json.load(open(args.b, encoding="utf-8"))
    if pa.get("scale_version") != pb.get("scale_version"):
        print("ВНИМАНИЕ: разные версии шкалы (%s vs %s) — сравнение нечестное, обновите скилл у обоих."
              % (pa.get("scale_version"), pb.get("scale_version")))
    na, nb = args.names or ("Воин A", "Воин B")

    print("=" * 64)
    print("PROMPT WARRIOR · ДУЭЛЬ · SCALE %s" % pa.get("scale_version"))
    print("=" * 64)
    print("%-30s | %s" % (na, nb))
    print("%-30s | %s" % (pa["title"]["ru"], pb["title"]["ru"]))
    ma, mb = pa["metrics"], pb["metrics"]
    print("%-30s | %s" % ("%s реплик, ур. %s" % (ma["messages"], pa["level"]),
                          "%s реплик, ур. %s" % (mb["messages"], pb["level"])))
    print("-" * 64)

    ga = {g["id"]: g for g in pa.get("gauges", [])}
    gb = {g["id"]: g for g in pb.get("gauges", [])}
    for gid in ga:
        if gid not in gb:
            continue
        a, b = ga[gid], gb[gid]
        lead = "<" if a["value"] > b["value"] else (">" if b["value"] > a["value"] else "=")
        print("%-12s %s %3d  %s  %3d %s" % (a["ru"], bar(a["value"]), a["value"], lead, b["value"], bar(b["value"])))

    duel_metrics = [("медиана слов", "median_words_voice"), ("verify %", "verify_pct"),
                    ("мат/1000 слов", "profanity_per_1000_words"), ("ночь %", "night_share_pct"),
                    ("похвала %", "praise_pct"), ("прерывания/100", "interruptions_per_100")]
    print("-" * 64)
    for label, key in duel_metrics:
        va, vb = ma.get(key), mb.get(key)
        if va is None or vb is None:
            continue
        print("%-18s %10s | %-10s" % (label, va, vb))

    aa = {x["id"] for x in pa["achievements"]}
    ab = {x["id"] for x in pb["achievements"]}
    only_a = [x["ru"] for x in pa["achievements"] if x["id"] not in ab]
    only_b = [x["ru"] for x in pb["achievements"] if x["id"] not in aa]
    both = len(aa & ab)
    print("-" * 64)
    print("Ачивки: общих %d · только у %s: %s · только у %s: %s"
          % (both, na, ", ".join(only_a) or "—", nb, ", ".join(only_b) or "—"))
    print("=" * 64)


if __name__ == "__main__":
    main()
