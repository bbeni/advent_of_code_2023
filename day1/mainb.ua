IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./input.txt"
OneMask ← ⍥(↥↻¯1.)⧻"one"⌕"one"

# ≡⍜⊔ ∘ IL
# ⊜□ ¬⍥(↥↻¯1.)⧻"one"⌕"one". ⊔ .□$ ttwo1oneoneasdf12

# this takes the first and last digit of a boxed string and adds them
regex "\\d|one|two|three|for|five|six|seven|eight|nine" .⊔ □$ ttwo1one9oneasdf12nine
:×1 ↥∵(⊔≍□"one"),∵(⊔≍□"1").
⊙↥:×2 ↥∵(⊔≍□"two"),∵(⊔≍□"2").
⊙↥:×3 ↥∵(⊔≍□"three"),∵(⊔≍□"3").
⊙↥:×4 ↥∵(⊔≍□"four"),∵(⊔≍□"4").
⊙↥:×5 ↥∵(⊔≍□"five"),∵(⊔≍□"5").
⊙↥:×6 ↥∵(⊔≍□"six"),∵(⊔≍□"6").
⊙↥:×7 ↥∵(⊔≍□"seven"),∵(⊔≍□"7").
⊙↥:×8 ↥∵(⊔≍□"eight"),∵(⊔≍□"8").
⊙↥:×9 ↥∵(⊔≍□"nine"),∵(⊔≍□"9").
+ ⊢ ⇌:⊢ .;:;