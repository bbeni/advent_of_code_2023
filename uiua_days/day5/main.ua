# string <- string
Strip ← ▽ ×⍜(⊟⇌) ≡\↥.≠@ .
# array(boxes) <- char string
SplitBy ← ⊜□≠,
# array(boxes) <- string string
SplitByS ← ⊜□ ¬∊ ,
# maps all next neightbours incl diagonals of binary matrix
Neighbours ← >0 /+ ≡↻ ☇1 ⊞⊂.-1⇡3 ↯ [9 .] ⧻.
# Sparse 1, 2d arrat<- N
Sparse ← ⁅⊞⋅⋅(÷1.9⚂) .⊚

Text ← &fras $ test.txt
# Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
InpLines ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./test.txt"

# ## Good Luck !
Seeds ← ∵(parse ⊔) ↘ 1SplitBy @  ⊔ ⊢ InpLines
Maps ← ∵⍜⊔ (∵⊔ ↯ 1) ∵⍜⊔ (∵⍜⊔(⊐∵parse SplitBy @ )) ∵(□ ↘1 ⊔) SplitBy □"" ↘ 2 InpLines

# ∵(dump∘ /(|2 ⊂ ⍉ dump∘ ⊞+ ⇡ ⊃(⊢⇌)(↙2)) ↯ 2_3 ⊔)Maps
# ≡(/⊂⊔) ≡(□dump∘ ⍉+[.]:↙2:⇡ ⊢⇌.) ↯ ¯1_3 ⊔⊢ .Maps

↙ 2 Seeds
↯ ¯1_3 ⊔ ⊢ Maps

=1\+ ⊂: ⊚ +100 ¯ ⧻.⍘⊚ \+ . ↯ 2_1 ↙ 2 Seeds

≡(=1\+ ⊂: ⊚ +100 ¯ ⧻.⍘⊚ \+ ↙ 1) ↯ 2_¯1 Seeds

¤ [1 4 6 23 2 3 23 23]
