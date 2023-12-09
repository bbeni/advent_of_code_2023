# Text ← &fras $ test.txt
Text ← &fras $ input.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
Im ← ∵⍜⊔ (⊜□¬∊, ";" ↘1⊔⊢⇌⊜□≠, @:) Lines

ParseColor! ← ∵⍜⊔ ∵(⍣(parse⊢)⋅⋅0 ⇌ regex ^0)
ParseColor!("(\\d+) red") Im
ParseColor!("(\\d+) green") Im
ParseColor!("(\\d+) blue") Im
:/+×:+1⇡⧻.¬⊐∵⍜⊔ /↥ /↥ >[12 13 14].⇌⊂⊂¤

# Part Two
/+/× ∵(/↥⊔)
