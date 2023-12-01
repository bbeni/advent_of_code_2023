IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./input.txt"
# IL ← ⊕□⍜▽¯:\+.=,@\n ▽¬∊,"\r" &fras "./test.txt"

# Part A
≡/+. ∵(≡parse⊔)≡⍜⊔(▽0_1_1) ▽ >0☇0∵△ .≡⍜⊔ (regex "(\\d).*(\\d)") IL
=0☇0∵△≡⍜⊔ (regex "(\\d).*(\\d)") IL
≡⍜⊔(▽0_1) ▽ >0☇0∵△ .∵⍜⊔ (regex ".*(\\d)") IL
+⊙.;:/+ ⊢ ⍉ .+≡⇌: ≡×10.:;: +×10 . /+/+ ∵/+∵(∵parse ⊔) ▽:
:

# Part B not working properly ...
# IL
# ⊜□ ≠, @ $ one two three for five six seven eight nine
# |one|two|three|for|five|six|seven|eight|nine
Reg ← "(\\d|one|two|three|for|five|six|seven|eight|nine).*(\\d|one|two|three|for|five|six|seven|eight|nine)"
# [□"9fiveonevmxhtndtfzmnxvtjkmr51six" □"9onevmxhtndtfzmnxvtjkmr51six" □"9onevmxhtndtfzmnxvtjkmr51six"]

IL
:×1 ≡⍜⊔ (↥ =□"1": =□"one". ↘1regex Reg).
:×2 ≡⍜⊔ (↥ =□"2": =□"two" . ↘1regex Reg).
:×3 ≡⍜⊔ (↥ =□"3": =□"three". ↘1regex Reg).
:×4 ≡⍜⊔ (↥ =□"4": =□"four". ↘1regex Reg).
:×5 ≡⍜⊔ (↥ =□"5": =□"five". ↘1regex Reg).
:×6 ≡⍜⊔ (↥ =□"6": =□"six". ↘1regex Reg).
:×7 ≡⍜⊔ (↥ =□"7": =□"seven". ↘1regex Reg).
:×8 ≡⍜⊔ (↥ =□"8": =□"eight". ↘1regex Reg).
:×9 ≡⍜⊔ (↥ =□"9": =□"nine". ↘1regex Reg).
++++++++;
▽>0∵⧻.
≡/+ ⍉ ×[10 1] ⍉ ≡⊔
/+
