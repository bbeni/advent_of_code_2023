# Text ← &fras $ test.txt
Text ← &fras $ input.txt

Lines ← ⊜□¬ ∊,"\r\n" Text
Im ← ∵⍜⊔ (⊜□¬∊, ";" ↘1⊔⊢⇌⊜□≠, @:) Lines
R ← regex "(\\d+) red"
G ← regex "(\\d+) green"
B ← regex "(\\d+) blue"

∵⍜⊔ ∵(⍣(parse⊢)⋅⋅0 ⇌ R) Im
∵⍜⊔ ∵(⍣(parse⊢)⋅⋅0 ⇌ G) Im
∵⍜⊔ ∵(⍣(parse⊢)⋅⋅0 ⇌ B) Im
.⇌⊂⊂¤
>[12 13 14]
.¬⊐∵⍜⊔ /↥ /↥
+1⇡⧻
:
/+ ×

:

# Part Two
/+/× ∵(/↥⊔)
