# Text ← &fras $ inputs/te4.txt
Text ← &fras $ inputs/in4.txt
Lines ← ⊜□¬ ∊,"\r\n" Text

Trim ← ▽×⍜(⊟⇌)≡\↥.≠@ .
Cards ← ∵°□∵⍜°□(∵⍜°□(⊜⋕ ¬∊, " " Trim)) ∵⍜°□ (⊜□¬∊, "|" ↘1°□⊢⇌⊜□≠, @:) Lines
Win ← ⊐≡⊡0 Cards
Yours ← ⊐≡⊡1 Cards
/+ ⌊ ⁿ:2 ≡(-1/+ .∊) Win Yours

:
# PArt Two

⍉ ⊟:⊙:⇡⧻,= ..≡/+
/+ ∧(+× ⊙(⊡⊙.:) ⍜⊏(+1) :≠., ++1⇡ ⊃⊢(,:⊢⇌))
