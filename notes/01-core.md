# Round decimal amounts explicitly: implementation

## What the example does

Construct Decimal from strings to avoid importing binary float error. ROUND_HALF_UP is one rounding policy; financial contracts may require another.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "amount": "2.675",
  "unit": "0.01"
}
```

Expected result:

```json
"2.68"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
