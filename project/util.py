character_vi = "áảạàăắằặẳâậầấẩđẹèéẻêệềếểịìíỉọòóỏôộồốổơớờợởuụùúủưựừứử"
character_vi = set(list(character_vi))



def classify(text, threshshold):
    count = 0
    text = text.lower()
    for i, c in enumerate(text):
        if c in character_vi:
            count += 1
    if count >= threshshold:
        return True
    return False