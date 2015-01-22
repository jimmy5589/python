def clip(lo, x, hi):
    return min(max(lo, x), hi)
    
print str(clip(2,-2,8))
print str(clip(2,6,8))
print str(clip(2,10,8))
