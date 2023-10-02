class CQCode:
    def __init__(self, cq_type, content):
        self.cq_type = cq_type
        self.content = content

    def dump(self):
        if self.cq_type == "face":
            return "[CQ:face,id=" + str(self.content) + "]"
        elif self.cq_type == "at":
            return "[CQ:at,qq=" + str(self.content) + "]"
        elif self.cq_type == "music":
            return "[CQ:music,type=163,id=" + str(self.content) + "]"
        elif self.cq_type == "image":
            return "[CQ:image,file=" + str(self.content) + "]"
        elif self.cq_type == "poke":
            return "[CQ:poke,qq=" + str(self.content) + "]"
