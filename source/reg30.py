def analyze_text_0(text):
    """
    Parameters
    ----------
    text : str
        This is the text that needs to be analyzed.

    Returns
    -------
    A dictionary where the (key, value) pair are as follows:
        key: the length of a word in the text
        value: the number of words of this length that are in the text
    """
    ret = {}
    words = text.split(' ')
    for word in words:
        word_len = len(word)
        if word_len not in ret:
            ret[word_len] = 1
        else:
            ret[word_len] += 1
    return ret

print(analyze_text_0('This is the text that needs to be analyzed.'))            
print(analyze_text_0('"I have of late—but wherefore I know not—lost all my mirth, forgone all custom of exercise; and indeed it goes so heavily with my disposition that this goodly frame, the earth, seems to me a sterile promontory. This most excellent canopy the air, look you, this brave o’erhanging, this majestical roof fretted with golden fire—why, it appears no other thing to me than a foul and pestilent congregation of vapours."'))            
        