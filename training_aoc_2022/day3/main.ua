# [⍥@\u2665 75]
IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./input.txt"
ILS ← ⊜□ =⊃(≠ @\r)(≠ @\n) &fras "./input.txt"

InpLines ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./test.txt"
InpLinesStrip ← ⊜□ =⊃(≠ @\r)(≠ @\n) &fras "./test.txt"
Split ← ⊔∵⍜⊔(⊜□≠@ .)IL

Len ← /+=.
TakeFirstHalfString ← ↙ ÷ 2 Len.
TakeLastHalfString ← ↘ ÷ 2 Len.

Priority ← + ×58 <0 .+1-@a
MatchingItemValue ← /↥ × =,⊡0: ⊡1 .⍉ Priority ↯ [÷2⊙2] Len ♭.⊠⊂ ⊃TakeFirstHalfString TakeLastHalfString

/+ ∵(MatchingItemValue⊔)♭ ⍉≡⊔Split
