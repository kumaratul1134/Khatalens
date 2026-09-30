from guardrails import valid_gstin, verify
def test_gstin():
    assert valid_gstin("27AAPFU0939F1ZV")
    assert not valid_gstin("27AAPFU0939F1ZX")
def test_verify():
    ok = {"gstin":"27AAPFU0939F1ZV","taxable":1000,"cgst":90,"sgst":90,"total":1180}
    assert verify(ok) == []
    assert "Totals do not reconcile" in verify({**ok,"total":1500})
