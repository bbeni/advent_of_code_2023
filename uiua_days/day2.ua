# Text ← &fras $ inputs/te2.txt
Text ← &fras $ inputs/in2.txt
Lines ← ⊜□¬ ∊,"\r\n" Text
Im ← ∵⍜°□ (⊜□¬∊, ";" ↘1°□⊢⇌⊜□≠, @:) Lines

ParseColor! ← ∵⍜°□ ∵(⍣(⋕⊢)⋅⋅0 ⇌ regex ^0)
ParseColor!("(\\d+) red") Im
ParseColor!("(\\d+) green") Im
ParseColor!("(\\d+) blue") Im
:/+×:+1⇡⧻.¬⊐∵⍜°□ /↥ /↥ >[12 13 14].⇌⊂⊂¤

# Part Two
/+/× ∵(/↥°□)
