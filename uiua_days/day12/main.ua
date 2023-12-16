# Get Lines of '\r\n' separated text
Lines ← ⊜□¬ ∊,"\r\n"
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

# Convolution 2D by Odd NxN matrix
# ↯ 4_4 0
# ☇ 1 ⊞⊟.-⌊÷2⧻.⇡⧻.↯3_3 2 Sparse 10
# ↯3_3 2 Sparse 10

Text ← &fras $ ../../inputs/te12.txt
# Text ← &fras $ ../../inputs/in12.txt

Lines Text
