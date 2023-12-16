# Text ← &fras $ inputs/te3.txt
Text ← &fras $ inputs/in3.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
NumbersMask ← ∊: +@0 ⇡10 ∵°□ Lines

# Part One
SymbolsMask ← ¬∊: ⊂ @. +@0 ⇡10 ∵°□ Lines
AdjMask ← >0 /+ ≡↻ ☇1 ⊞⊂.-1⇡3 ↯ [9 .] ⧻. SymbolsMask
Overlap ← ↧ AdjMask NumbersMask
AreParts ← ≡(/↥°□⊢) ↯ ¯1_1 ⊜(□) ∩♭ NumbersMask Overlap
Parts ← ⊐/⊂ ≡(□⊜⋕) NumbersMask ∵°□ Lines
/+ ▽ AreParts Parts

# Part Two
GearsMask ← =: @* ∵°□ Lines
GearIDMask ← ×⍜♭ \+ .GearsMask
GearIDAdj ← /+ ≡↻ ☇1 ⊞⊂.-1⇡3 ↯ [9 .] ⧻. GearIDMask
⊜(⋕) ♭NumbersMask ⊐/⊂ Lines
⊜(/↥) ♭NumbersMask ♭GearIDAdj
/+/× ⍉ ∵((∘|[0 0]) ⊢<2 △ .°□) ↘1 ⊕(□)
