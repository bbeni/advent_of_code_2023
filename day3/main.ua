# Part One
# Text ← &fras $ test.txt
Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
SymbolsMask ← ¬∊: ⊂ @. +@0 ⇡10 ≡∵⊔ Lines
NumbersMask ← ∊: +@0 ⇡10 ≡∵⊔ Lines
AdjMask ← >0 /+ ≡↻ ☇1 ⊞⊂.-1⇡3 ↯ [9 .] ⧻. SymbolsMask

A ← ↧ AdjMask NumbersMask
AreParts ← ≡(/↥⊔⊢) ↯ ¯1_1 ⊜(□) ∩♭ NumbersMask A

Parts ← ⊐/⊂ ≡(□⊜parse) NumbersMask ≡∵⊔ Lines
/+ ▽ AreParts Parts

# Part Two (pure)
# Text ← &fras $ test.txt
Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text

NumbersMask ← ∊: +@0 ⇡10 ≡∵⊔ Lines
GearsMask ← =: @* ≡∵⊔ Lines
GearIDMask ← ×⍜♭ \+ .GearsMask
GearIDAdj ← /+ ≡↻ ☇1 ⊞⊂.-1⇡3 ↯ [9 .] ⧻. GearIDMask

⊜(/↥) ♭NumbersMask ♭GearIDAdj
⊜(□) ♭NumbersMask ⊐/⊂ Lines
/+/× ⍉ ∵((∵(⊔parse)|[0 0]) ⊢<2 △ .⊔) ↘1 ⊕(□) :
