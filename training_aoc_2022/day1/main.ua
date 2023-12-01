# [⍥@\u2665 75]
IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./input.txt"
ILS ← ⊜□ =⊃(≠ @\r)(≠ @\n) &fras "./input.txt"

InpLines ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./test.txt"
InpLinesStrip ← ⊜□ =⊃(≠ @\r)(≠ @\n) &fras "./test.txt"
Split ← ⊔∵⍜⊔(⊜□≠@ .)InpLines

# solution to day 1 part a
/↥ .⊐∵⍜⊔ (∧(+parse) :0) ⊜□≠□"" .⊔IL

# solution b
/+ ↙ 3 ⊏⍖.:
