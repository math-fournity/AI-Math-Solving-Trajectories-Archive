# Audit Task

You are an analysis quality auditor. You will NOT re-analyze any problem.
You will check the QUALITY of an existing analysis result.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
- Output your audit directly in your response (in this TUI).
- End your audit with a line containing exactly: `### AUDIT COMPLETE`

## Audit Task

You are given one analysis result (produced by a previous AI that analyzed a math problem).
Your job is to check the QUALITY of this analysis result — NOT to re-analyze the problem.

You do NOT have the original problem, the standard solution, or the AI's thinking.
You only have the analysis result itself. Check its quality on 5 dimensions.

### Dimension A: Field Completeness

- **A1**: dimension1_verdict is non-empty AND is one of: DIRECTION_ERROR, TOKEN_LIMIT, CONNECTION_ERROR, PARTIAL_PROGRESS
- **A2**: dimension1_explanation is non-empty AND length >= 50 characters
- **A3**: dimension2_turning_point_type is non-empty (when d1 is DIRECTION_ERROR or PARTIAL_PROGRESS) AND is one of: mod_p_grouping, mod_p_non_obvious, quadratic_residue_euler, lte_lemma, p_adic_valuation, multi_step_mod_p, crt, permutation_polynomial, finite_field_structure, other
- **A4**: dimension2_explanation is non-empty AND length >= 50 characters
- **A5**: ai_direction_summary is non-empty
- **A6**: standard_solution_key_technique is non-empty

### Dimension B: Content Integrity

- **B1**: dimension1_explanation and dimension2_explanation do NOT contain XML tag leaks (strings like `</dimension` or `<dimension`)
- **B2**: dimension1_explanation and dimension2_explanation do NOT contain template placeholder leaks (strings like "1-3 sentences", "ONE_OF:", "Your 1-3 sentence")
- **B3**: dimension1_explanation and dimension2_explanation are not too short (>= 50 characters)

### Dimension C: Internal Consistency

- **C1**: d1/d2 logical consistency — when d1=CONNECTION_ERROR, d2 may be null; when d1=DIRECTION_ERROR or PARTIAL_PROGRESS or TOKEN_LIMIT, d2 should have a value
- **C2**: dimension1_explanation is consistent with dimension1_verdict — the failure type described in d1_exp matches the d1 label (e.g., if d1=DIRECTION_ERROR, d1_exp should describe a wrong direction, not a token shortage)
- **C3**: dimension2_explanation is consistent with dimension2_turning_point_type — the technique described in d2_exp matches the d2 label (e.g., if d2=mod_p_grouping, d2_exp should describe mod p grouping, not CRT)

### Dimension D: Operability (only checked when d1=DIRECTION_ERROR or PARTIAL_PROGRESS)

**IMPORTANT**: D checks are ONLY evaluated when d1=DIRECTION_ERROR or d1=PARTIAL_PROGRESS.
When d1=CONNECTION_ERROR or d1=TOKEN_LIMIT, output "N/A — d1 is CONNECTION_ERROR/TOKEN_LIMIT" for D1-D4,
and these checks do NOT affect the audit status.

- **D1**: dimension1_explanation is operable — length >= 100 characters AND contains at least one action verb (identified, missed, explored, used, went, attempted, tried, failed, overlooked, ignored)
- **D2**: dimension2_explanation is operable — length >= 100 characters AND contains at least one mathematical term
- **D3**: ai_direction_summary is operable — it describes what direction the AI actually took (not just "the AI failed")
- **D4**: standard_solution_key_technique is operable — it describes the specific technique of the standard solution (not just "the standard solution uses a clever method")

### Dimension E: Duplication Flag

- **E1**: Mark whether this problem_id appears to have multiple analysis results (you cannot determine this from a single result, so always output "UNKNOWN — check via script")

## Audit Status Determination

Based on A-E checks, determine the overall audit status:

- **PASS**: A1-A6 all pass + B1-B3 all pass + C1-C3 all pass (d1 is CONNECTION_ERROR or TOKEN_LIMIT — D checks are N/A)
- **PASS_SELECTABLE**: PASS + d1=DIRECTION_ERROR + D1-D4 all pass (suitable for entering selection pool)
- **FAIL_PARSE_ERROR**: A1 fails (d1 is null or invalid)
- **FAIL_INCOMPLETE**: Any of A2-A6 fails
- **FAIL_CONTENT_CORRUPT**: B1 or B2 fails (XML leak or placeholder leak)
- **FAIL_INCONSISTENT**: Any of C1-C3 fails
- **PASS_NOT_SELECTABLE**: A-C all pass + d1=DIRECTION_ERROR/PARTIAL_PROGRESS + D1-D4 any fail (result is valid but not operable enough for selection)

## Output Format

Output your audit as a single XML block. Replace each placeholder with your actual audit.

**IMPORTANT**: Each XML tag must be closed with the EXACT matching closing tag.

```xml
<audit>
  <analysis_result_key>2272968</analysis_result_key>
  <problem_id>polymath_00840</problem_id>
  <audit_status>ONE_OF: PASS, PASS_SELECTABLE, FAIL_PARSE_ERROR, FAIL_INCOMPLETE, FAIL_CONTENT_CORRUPT, FAIL_INCONSISTENT, PASS_NOT_SELECTABLE</audit_status>
  <check_results>
    <A1>PASS or FAIL: one-sentence reason</A1>
    <A2>PASS or FAIL: one-sentence reason</A2>
    <A3>PASS or FAIL: one-sentence reason</A3>
    <A4>PASS or FAIL: one-sentence reason</A4>
    <A5>PASS or FAIL: one-sentence reason</A5>
    <A6>PASS or FAIL: one-sentence reason</A6>
    <B1>PASS or FAIL: one-sentence reason</B1>
    <B2>PASS or FAIL: one-sentence reason</B2>
    <B3>PASS or FAIL: one-sentence reason</B3>
    <C1>PASS or FAIL: one-sentence reason</C1>
    <C2>PASS or FAIL: one-sentence reason</C2>
    <C3>PASS or FAIL: one-sentence reason</C3>
    <D1>PASS or FAIL: one-sentence reason</D1>
    <D2>PASS or FAIL: one-sentence reason</D2>
    <D3>PASS or FAIL: one-sentence reason</D3>
    <D4>PASS or FAIL: one-sentence reason</D4>
    <E1>UNKNOWN — check via script</E1>
  </check_results>
  <issues_found>Comma-separated list of issues, or "none"</issues_found>
</audit>
```

After the XML block, output exactly: `### AUDIT COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### AUDIT COMPLETE)
- Each opening tag must have a matching closing tag
- Output exactly ONE value for each field
- Be strict: if a field is empty, null, or too short, FAIL the corresponding check
- For C2/C3: read the explanation text carefully and judge whether it semantically matches the label — this requires understanding, not keyword matching

## Analysis Result to Audit

  problem_id: polymath_00840
  dimension1_verdict: PARTIAL_PROGRESS
  dimension1_explanation: The AI found the correct solution (a,b)=(1,1) with c=2 early on, and was systematically working to prove uniqueness via case enumeration (c=1,2,3,...,12) and asymptotic recurrence analysis. However, it missed the standard solution's crucial p-adic valuation approach on b-1, instead relying on laborious brute-force enumeration that consumed its entire token budget without completing the general proof for all c>2.
  dimension2_turning_point_type: p_adic_valuation
  dimension2_explanation: The standard solution's key turning point is showing that 2^{t+1} | b-1 must hold for all t, which forces b=1 via 2-adic valuation (only b=1 has b-1 divisible by arbitrarily high powers of 2). This elegantly pins down b without enumeration, after which Fermat's Little Theorem on large primes p dividing 2^n a + 1 forces 2a+1 | 3, giving a=1.
  ai_direction_summary: The AI's thinking went in the direction of exhaustive case-by-case enumeration of c values combined with asymptotic growth-rate analysis of the recurrence q_{n+1} = (c·q_n·d_n - (c-1))/d_{n+1}, rather than using p-adic valuations to directly constrain b.
  standard_solution_key_technique: The standard solution uses 2-adic valuation (v_2) analysis on b-1 to force b=1, then applies Fermat's Little Theorem with large primes to constrain a, avoiding enumeration entirely.
  confidence: high
