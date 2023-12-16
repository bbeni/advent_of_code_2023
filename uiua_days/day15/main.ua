# part one
/+ ⊜(/(◿ 256×17+) ⊂ 0 -@\0) ≠, @, ↘ ¯1 &fras "../../inputs/in15.txt"

# part two
HASH ← /(◿ 256×17+) ⊂ 0 -@\0
BoxSeq ← ⊜(HASH ▽ ≥@A.) ≠, @, &fras "../../inputs/te15.txt"
LabelSeq ← ⊜(□ ▽ ≥@A.) ≠, @, &fras "../../inputs/te15.txt"
OperationSeq ← ⊜(⍣⋕⋅⋅0 ▽ ↧ ≥@0,≤@9.) ≠, @, &fras "../../inputs/te15.txt"

# appending
# ⍜(°□ ⊏ 0)⊂: 23 {[1] [] [2] []}

∧(⍜(°□ ⊏12)⊂:;) BoxSeq LabelSeq ♭ ↯ 256 {[]}

# ∧(⊃(+)(+⊙⋅∘)) [1 2 3] 2 3
# ⍜(°□ ⊏) ⊙⊂ 0 23 {[1] [] [2] []}
