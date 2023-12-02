Text ← &fras $ test.txt
# Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
LinesR ← ⊕□⍜▽¯:⌈÷2 \+.∊,"\r\n" Text
GroupedLinesByWS ← ⊕□⍜▽ ¯:\+.=□"".LinesR
