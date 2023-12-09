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

# Text ← &fras $ test.txt
Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text

### Good Luck !