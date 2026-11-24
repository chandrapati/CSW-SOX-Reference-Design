"""Framing text for SOX ITGC. Everything else is read from the design."""

DESIGN = 'CSW-SOX-Reference-Design.md'

TREE = {'kicker': 'SOX ITGC',
 'rail': ['Label queries keep scope membership current automatically',
          'Every in-scope workload resolves into exactly one scope',
          'The tree is the boundary an assessor will ask you to defend'],
 'sub': 'The scope hierarchy this design recommends, with label-driven membership so the '
        'boundary stays current as the estate changes.',
 'takeaway': 'Scope membership is <b>label-driven, not a static list</b>, so the boundary '
             'stays accurate as the estate changes. Scope accuracy is itself evidence in most '
             'assessments.',
 'takeaway_tag': 'Key Takeaway',
 'title': 'Scope Architecture',
 'title_tail': '&mdash; SOX ITGC'}

WORKFLOW = {'caution': 'User access reviews and entitlement recertification, segregation of duties within '
            'the financial application, change authorisation workflow, SDLC and program '
            'development controls, backup and recovery testing, management review controls, '
            'entity-level COSO controls, and external auditor attestation all require separate '
            'programmes.',
 'caution_label': 'Boundary &rsaquo;',
 'kicker': 'SOX ITGC',
 'rail': ['Machine-generated flow evidence, not hand-drawn diagrams',
          'Simulation proves the policy before anything is enforced',
          'Quarterly packs carry the evidence between assessments'],
 'sub': 'From agent coverage to continuous proof between assessments &mdash; exports map to '
        'control IDs in the Reporting & Evidence section.',
 'takeaway': 'CSW turns observed traffic into designed isolation and keeps producing evidence '
             'after the project ends. <b>The quarterly pack is the deliverable</b> &mdash; it '
             'is what an assessor consumes without a live walkthrough.',
 'title_tail': '&mdash; SOX ITGC'}

PHASES = None
