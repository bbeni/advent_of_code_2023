IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "inputs/in1.txt"
D ← "\\d"
R ← "one|two|three|four|five|six|seven|eight|nine"
ReverseMatchRe ← ∵⇌ regex ⊂⊂D@|⇌R ⇌
MatchRe ← regex ⊂⊂D@|R
OneToNine ← ⊜□ ≠, @| R
Parse ← +1 ⊗ :OneToNine □
∵(⊢ MatchRe) IL
∵(⊢ ReverseMatchRe) IL
/+/+ ⍜(⊏ [1])(×10) ∵(⍣⋕ (Parse;:) °□) ⊟
