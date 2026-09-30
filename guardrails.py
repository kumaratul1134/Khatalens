"""KhataLens guardrails: deterministic checks that verify LLM-extracted invoice data."""
import re
CS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def valid_gstin(g: str) -> bool:
    g = g.strip().upper()
    if not re.fullmatch(r"\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]", g):
        return False
    total, factor = 0, 2
    for c in reversed(g[:-1]):
        d = factor * CS.index(c)
        factor = 1 if factor == 2 else 2
        total += d // 36 + d % 36
    return CS[(36 - total % 36) % 36] == g[-1]

def totals_ok(taxable: float, cgst: float, sgst: float, igst: float, total: float, tol=1.0) -> bool:
    return abs(taxable + cgst + sgst + igst - total) <= tol

def verify(inv: dict) -> list:
    """Return a list of human-review flags (empty list = passed)."""
    flags = []
    if not valid_gstin(inv.get("gstin", "")):
        flags.append("Invalid GSTIN")
    if not totals_ok(inv["taxable"], inv.get("cgst", 0), inv.get("sgst", 0), inv.get("igst", 0), inv["total"]):
        flags.append("Totals do not reconcile")
    return flags
