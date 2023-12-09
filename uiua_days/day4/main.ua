# Text ← &fras $ test.txt
Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text

Trim ← ▽×⍜(⊟⇌)≡\↥.≠@ .
Cards ← ∵⊔∵⍜⊔(∵⍜⊔(⊜parse ¬∊, " " Trim)) ∵⍜⊔ (⊜□¬∊, "|" ↘1⊔⊢⇌⊜□≠, @:) Lines
Win ← ⊐≡⊡0 Cards
Yours ← ⊐≡⊡1 Cards
/+ ⌊ ⁿ:2 ≡(-1/+ .∊) Win Yours

:
# PArt Two

⍉ ⊟:⊙:⇡⧻,= ..≡/+
/+ ∧(+× ⊙(⊡⊙.:) ⍜⊏(+1) :≠., ++1⇡ ⊃⊢(,:⊢⇌))
