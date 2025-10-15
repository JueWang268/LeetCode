class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []
        curlen = 0
        curline = []
        for i in range(len(words)):
            if curlen + len(words[i]) > maxWidth:
                # every word we add, we added an extra emptyspace
                emptyspaces = maxWidth
                for w in curline:
                    emptyspaces -= len(w)
                gaps = len(curline) - 1
                linebuild = ""
                if gaps > 0:
                    gaplen, extra = divmod(emptyspaces, gaps)
                    for j in range(len(curline) - 1):
                        linebuild += curline[j]
                        linebuild += gaplen * " "
                        if j <= extra - 1:
                            linebuild += " "
                    linebuild += curline[-1]
                else: # only 1 element
                    linebuild = curline[0] + emptyspaces*" "
                out.append(linebuild)
                curlen = 0
                curline = []
            curlen += len(words[i]) + 1 # at least one space
            curline.append(words[i])
        # last line

        out.append(' '.join(curline) + (maxWidth-curlen+1)*" ")
        return out